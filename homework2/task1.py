"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
import unicodedata
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    longest_diverse_words = []
    mem = ''
    with open(file_path) as f:
        for line in f:
            data = line.strip().encode().decode('unicode-escape').split()
            print(data)
            for word in data:
                check = data[-1]
                if check[-1] == '-':
                    mem = check[0:-1]
                    continue
                if mem != '':
                    word = mem + word
                    mem = ''
                # if word in longest_diverse_words:
                #     continue
                for symbol in word:
                    if unicodedata.category(symbol).startswith('P'):
                        word = word.replace(symbol, '')
                if len(longest_diverse_words) < 10:
                    longest_diverse_words.append(word)
                else:
                    for element in longest_diverse_words:
                        if len(set(element)) < len(set(word)):
                            longest_diverse_words.remove(element)
                            longest_diverse_words.append(word)
        print(longest_diverse_words)



def get_rarest_char(file_path: str) -> str:
    ...


def count_punctuation_chars(file_path: str) -> int:
    ...


def count_non_ascii_chars(file_path: str) -> int:
    ...


def get_most_common_non_ascii_char(file_path: str) -> str:
    ...


get_longest_diverse_words('data.txt')
s = 'Souveränitätsansprüch'
print(s.lower())