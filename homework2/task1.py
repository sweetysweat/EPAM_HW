"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path) as f:
        for line in f:
            data = line.encode('utf-8').decode('utf-8')
            print(data)


def get_rarest_char(file_path: str) -> str:
    ...


def count_punctuation_chars(file_path: str) -> int:
    ...


def count_non_ascii_chars(file_path: str) -> int:
    ...


def get_most_common_non_ascii_char(file_path: str) -> str:
    ...


s = '\u00bbJetzt und hier\u00ab'
d = s.strip().encode()
print(d)
# get_longest_diverse_words('data.txt')

with open('data.txt') as f:
    for line in f:
        print(line.encode())
