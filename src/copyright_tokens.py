import os
import pickle
import re
import pandas as pd
import glob


def extractCopyrightComments(file_paths):

    forbidden_tokens = [
        "free software",
        "licensed by",
        "licensed to",
        "licensed under",
        "distributed under",
        "license",
        "licence"
    ]

    search_tokens = [
    "copyright",
    "confidential",
    "penalty",
    "following conditions are met",
    "created by",
    "do not modify this file",
    '"as is"',
    'software is provided "as is"',
    "provided by",
    "without warranty of any kind",
    "warranties of merchantability",
    "damages or other liability",
    "fitness for a particular purpose and noninfringement",
    "(c)",
    ]
    
    noCopyright_tokens = [
        # "do not share this code",
        # "do not share this file",
        # "do not share", Maybe try using the commented keywords, but there are a lot of bogus comments
        "please do not share, copy, edit or distribute without owner's permission",
        "please do not share, copy, edit or distribute",
        "please do not share, copy",
        "please do not share"

    ]

    for file_path in file_paths:
        copyright_comments = []
        noCopyright_comments = []
        root, _ = os.path.splitext(file_path)
        file_name = os.path.basename(root)
        for elem in pd.read_pickle(file_path):
            try:
                lower_comm = elem.lower()
                comment = lower_comm.replace("\n", " ")
                if comment != "":
                    if re.search(r'\b' + 'no license' + r'\b', comment):
                        copyright_comments.append(elem)
                    elif not any(token in comment for token in forbidden_tokens) and any(token in comment for token in search_tokens):
                        copyright_comments.append(elem)
                    
                    if any(token in comment for token in noCopyright_tokens) and not any(token in comment for token in forbidden_tokens):
                        noCopyright_comments.append(elem)
                    elif any(token in comment for token in noCopyright_tokens) and re.search(r'\b' + 'license' + r'\b', comment):
                        noCopyright_comments.append(elem)
                    elif any(token in comment for token in noCopyright_tokens) and re.search(r'\b' + 'licence' + r'\b', comment):
                        noCopyright_comments.append(elem)
            except UnicodeEncodeError:
                continue

        with open(f'{file_name}_Copyright.pkl', 'wb') as save_file:
            pickle.dump(copyright_comments, save_file)

        with open(f'{file_name}_NoCopyright.pkl', 'wb') as save_file:
            pickle.dump(noCopyright_comments, save_file)

if __name__ == "__main__":
    pickle_pattern = '*.pkl'
    pickle_file_paths = glob.glob(pickle_pattern)
    extractCopyrightComments(pickle_file_paths)


