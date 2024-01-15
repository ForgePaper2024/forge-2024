import json
import os
import pickle
import re
import pandas as pd
import glob


def strongCopyLeftLicenseInComments(file_paths):

    license_tokens = [
    "gnu general public license",
    "gnu gpl",
    "gpl",
    "gnu affero general public license",
    "affero general public license",
    "gnu agpl",
    "agpl",
]

    licenses_counter = ["No. of Strong Copyleft Licenses in Datasets' Comments\n"]
    for file_path in file_paths:
        counter = 0
        root, _ = os.path.splitext(file_path)
        file_name = os.path.basename(root)
        for comment in pd.read_pickle(file_path):
            try:
                if comment != "":
                    comment = comment.lower()
                    if any(re.search(r'\b' + token + r'\b', comment) for token in license_tokens):
                        if 'lesser' not in comment and 'lgpl' not in comment:
                            counter += 1
            except UnicodeEncodeError:
                continue
        print(f"{file_name} - {counter}")
        licenses_counter.append(f"{file_name} - {counter}\n")

    with open(f'StCopyLeftLicenseCount.json', 'w') as save_file:
        json.dump(licenses_counter, save_file, indent=2)




if __name__ == "__main__":
    pickle_pattern = '*.pkl'
    pickle_file_paths = glob.glob(pickle_pattern)
    strongCopyLeftLicenseInComments(pickle_file_paths)
