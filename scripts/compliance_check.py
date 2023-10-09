import itertools
import json
import os
import re
from glob import glob
from typing import List

import marvin
from bs4 import BeautifulSoup
from config import ENTITIY_FOLDERS
from loguru import logger
from marvin import ai_fn
from pydantic import BaseModel
from tabulate import tabulate

COMPLIANCE_CHECK_FOLDER = {
    "SPD41a": "alignments/SPD-41a",
    "FAIR": "alignments/FAIR",
}


class compliant_statements(BaseModel):
    policy: str
    statements: list[str]


marvin.settings.openai.api_key = os.environ.get("API_KEY")


# @ai_fn
@ai_fn(model="gpt-4")
def bulk_compliance_checker(
    policies: list[str], statements: list[str]
) -> list[compliant_statements]:
    """
    For each policy given, find the statements that DIRECTLY support and compliant with the policy.
    e.g: if policy is "Data shall be made publicly available, free in open, machine-readable formats [III.C.ii–iv]"
    a compliant statement for the above policy is A1.1.3 Adhere to community accepted standard machine readable data file formats
    a non-compliant statement for the above policy is A1.1.6  Adhere to community standard variable names, types, and unit(s), keywords
    returns list of compliant_statements objects
    """


def batch_run_bulk_compliance_checker(
    policies: List[str],
    statements: List[str],
    n: int,
) -> List[List[str]]:
    """
    Batch run bulk_compliance_checker function with n policies and n statements at a time
    """

    results: list[compliant_statements] = []
    batch_policies = (
        [policies[i : i + n] for i in range(0, len(policies), n)]
        if n < len(policies)
        else [policies]
    )
    batch_statements = [statements[i : i + n] for i in range(0, len(statements), n)]
    enum_policies = []
    enum_statements = []
    for batch_policy in batch_policies:
        for batch_statement in batch_statements:
            enum_policies.append(batch_policy)
            enum_statements.append(batch_statement)

    logger.info(f"Running bulk_compliance_checker with {len(enum_policies)} batches")
    try:
        results.extend(
            itertools.chain.from_iterable(
                bulk_compliance_checker.map(
                    policies=enum_policies, statements=enum_statements
                )
            )
        )
    except Exception as e:
        logger.error(f"Error running bulk_compliance_checker: {e}")

    logger.info(f"finished running bulk_compliance_checker with {len(results)} results")
    return results


def combine_results(
    compliant_statements: list[compliant_statements],
) -> list[compliant_statements]:
    compliant_statements_by_policy = {}
    for compliant_statement in compliant_statements:
        statements = compliant_statement.statements
        if statements:
            policy = compliant_statement.policy
            statements = compliant_statement.statements
            if policy not in compliant_statements_by_policy:
                compliant_statements_by_policy[policy] = []
            compliant_statements_by_policy[policy].extend(statements)

    # remove duplicates
    for policy, statements in compliant_statements_by_policy.items():
        compliant_statements_by_policy[policy] = list(set(statements))

    return compliant_statements_by_policy


def parse_markdown_file_table(
    mdfile_path: str, exclude_header: bool = True, use_cols: list = None
):
    """parses readme markdown file and returns a list of tuples with the table
    content

    Args:
        mdfile_path (str): path to readme markdown file to parse

    Returns:
        list: a list of tuples with the table content

    """

    def extract_table_from_non_html_md(md_content):
        lines = md_content.strip().split("\n")
        in_table = False
        table_data = []
        row_re = re.compile(r"^\|(.+?)\|$")

        for line in lines:
            if re.match(r"\|(-+\|)+", line):
                in_table = True
                continue

            if in_table:
                row_match = row_re.match(line)
                if row_match:
                    row_items = row_match.group(1).split("|")
                    row_items = tuple(item.strip() for item in row_items)
                    table_data.append(row_items)
                else:
                    in_table = False
        return table_data

    with open(mdfile_path, "r") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        table = soup.find("table")
        data = []
        try:
            rows = table.find_all("tr")
            headers = [
                re.sub("\s+", " ", th.text.strip()) for th in rows[0].find_all("th")
            ]
            for row in rows[1:]:
                cols = [
                    re.sub("\s+", " ", td.text.strip()) for td in row.find_all("td")
                ]
                data.append(tuple(cols))
            data.insert(0, tuple(headers))

        except AttributeError:
            data = extract_table_from_non_html_md(soup.text)

        if use_cols:
            data = [tuple(row[i] for i in use_cols) for row in data]
        return data[1:] if exclude_header else data


def run_dgf_extractions(save_file: str = None):
    dgf_dict = {}
    for dgf_folder in ENTITIY_FOLDERS:
        if not (os.path.exists(dgf_folder)):
            continue
        readme_files_loc = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            dgf_folder,
        )
        dgf_dict[dgf_folder] = {}
        for readme_file in glob(os.path.join(readme_files_loc, "*", "README.md")):
            # get folder name of readme file
            folder_name = os.path.basename(os.path.dirname(readme_file))
            dgf_dict[dgf_folder][folder_name] = parse_markdown_file_table(readme_file)
        # save to json

    return dgf_dict


def run_policy_extractions(save_file: str = None):
    compliance_check_dict = {}
    for policy in COMPLIANCE_CHECK_FOLDER.keys():
        readme_files_loc = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            COMPLIANCE_CHECK_FOLDER[policy],
        )
        compliance_check_dict[policy] = {}
        for readme_file in glob(os.path.join(readme_files_loc, "README.md")):
            # get folder name of readme file

            compliance_check_dict[policy] = parse_markdown_file_table(
                readme_file,
                exclude_header=False,
                use_cols=[0],
            )
            compliance_check_dict[policy] = [
                item for sublist in compliance_check_dict[policy] for item in sublist
            ][
                1:
            ]  # remove header
    if save_file:
        json.dump(
            compliance_check_dict,
            open("compliance_check.json", "w"),
            indent=4,
        )
    return compliance_check_dict


def compliance_check(n_comparisions: int = 10, debug: bool = False):
    n_times = 0
    dgf_dict = run_dgf_extractions()
    policy_dict = run_policy_extractions()
    policy_compliance = {}
    for policy in policy_dict.keys():
        policy_compliance[policy] = []
        for policy_item in policy_dict[policy]:
            policy_compliance[policy].append({policy_item: []})
    for policy_type, policy_items in policy_compliance.items():
        dgf_requirements = []
        for section in dgf_dict.keys():
            n_times += 1
            for subsection in dgf_dict[section].keys():
                for dgf_requirement, dgf_procedure in dgf_dict[section][subsection]:
                    dgf_requirements.append(
                        f"Requirement: {dgf_requirement} | Procedure: {dgf_procedure}"  # noqa: E501
                    )
        logger.info(
            f"Running compliance check for {policy_type} with {len(policy_items)} policies and {len(dgf_requirements)} requirements"
        )
        policy_items = [list(item.keys())[0] for item in policy_items]
        results = batch_run_bulk_compliance_checker(
            policy_items, dgf_requirements, n_comparisions or len(policy_items)
        )
        results = combine_results(results)
        policy_compliance[policy_type] = results
        if debug and n_times > 1:
            break

    return policy_compliance


if __name__ == "__main__":
    compiled_results = compliance_check()
    for policy_type, results in compiled_results:
        headers = [f"{policy_type} Requirements", "DGF requirements"]
        values = []
        for key, value in results:
            values.append([key, value])
        tabulate(values, headers=headers, tablefmt="grid")
