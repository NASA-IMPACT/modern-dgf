import re
import time
from glob import glob

import pandas as pd
import tqdm

import github_helper


def get_subfolders(folder):
    """
    Return the subfolders based on the given folder path.
    """
    subfolder_list = list(glob(folder + "*/*/", recursive=True))
    if not subfolder_list:  # for resources/*/
        subfolder_list = list(glob(folder + "*/", recursive=True))
    return subfolder_list


def extract_data_from_readme(subfolder):
    """
    Extract data from README.md within a given subfolder.
    """
    try:
        df = pd.read_html(subfolder + "README.md")[0]
    except ValueError:
        print("No table found in " + subfolder + "README.md")
        return None
    return df


def split_procedures_by_id(procedures):
    """
    Split procedures by ID and return a cleaned list.
    """
    split_by_id = re.split("(B\d.\d\.\d)", procedures)
    split_by_id = [i for i in split_by_id if i]

    procedures = [
        split_by_id[i] + split_by_id[i + 1] for i in range(0, len(split_by_id), 2)
    ]
    return [i.strip() for i in procedures if i]


folder_list = [
    "code",
    "data",
    "digital_content",
    "metadata",
    "resources/people/",
    "resources/storage/",
]

for folder in tqdm.tqdm(folder_list):
    for subfolder in get_subfolders(folder):
        df = extract_data_from_readme(subfolder)

        if df is not None:
            for _, row in df.iterrows():
                description, procedures = row.iloc[0], row.iloc[1]

                if isinstance(procedures, str):
                    procedures_list = split_procedures_by_id(procedures)
                    for procedure in procedures_list:
                        github_helper.create_issues(
                            "code-geek/dgf-playground",
                            title=procedure,
                            body=description,
                        )
                        time.sleep(5)