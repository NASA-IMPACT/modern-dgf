import re
import time
from glob import glob

import pandas as pd
import tqdm

import github_helper

folder_list = [
    "code",
    "data",
    "digital_content",
    "metadata",
    "resources/people/",
    "resources/storage/",
]


for folder in tqdm.tqdm(folder_list):
    subfolder_list = list(glob(folder + "*/*/", recursive=True))
    if not subfolder_list:  # for resources/*/
        subfolder_list = list(glob(folder + "*/", recursive=True))
    for subfolder in subfolder_list:
        try:
            df = pd.read_html(subfolder + "README.md")
        except ValueError:
            print("No table found in " + subfolder + "README.md")

        for row in df[0].iterrows():
            description = row[1].iloc[0]
            procedures = row[1].iloc[1]

            if isinstance(procedures, str):
                split_by_id = re.split("(B\d.\d\.\d)", procedures)
                split_by_id = [i for i in split_by_id if i]

                procedures = [
                    split_by_id[i] + split_by_id[i + 1]
                    for i in range(0, len(split_by_id), 2)
                ]
                procedures = [i.strip() for i in procedures if i]
                for procedure in procedures:
                    github_helper.create_issues(
                        "code-geek/dgf-playground",
                        title=procedure,
                        body=description,
                    )
                    time.sleep(5)
