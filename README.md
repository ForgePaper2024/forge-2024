# An Exploratory Investigation into Code License Infringements in Large Language Model Training Datasets - Reproduction package

This Repository contains the reproduction package for the paper submitted to FORGE 2024 with submission number 78.



## Scraped Repositories

The folder strong_copyleft contains the API output from the GitHub API, which was queried per language for the repositories used to generate the strong copyleft dataset in the paper.



## Tertiary Study

The results of the tertiary study are contained in the file [src](https://github.com/ForgePaper2024/forge-2024/tree/main/src)/Data Extraction Responses.csv.

This is the data we gathered and used to answer RQ 1.



## Comment search

The code used to search the leading comments from the dataset for strong copyleft licenses is contained in the file [src](https://github.com/ForgePaper2024/forge-2024/tree/main/src)/stcopyleft_licenses.py.

The code used to detect other copyright information is contained in the file [src](https://github.com/ForgePaper2024/forge-2024/tree/main/src)/copyright_tokens.py



## Comment Dataset

The code for extracting the leading comments, and the dataset itself will be released upon acceptance of this paper.
The Dataset itself will also be cleaned of all PII using the starcoder PII model.
