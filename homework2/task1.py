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
from collections import Counter
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    longest_diverse_words = []
    mem = ''
    with open(file_path) as f:
        for line in f:
            data = line.strip().encode().decode('unicode-escape').lower().split()
            for word in data:
                check = data[-1]
                if mem:
                    word = mem + word
                    mem = ''
                if check[-1] == '-':
                    mem = check[0:-1]
                for symbol in string.punctuation:
                    if unicodedata.category(symbol).startswith('P'):
                        word = word.replace(symbol, '')
                if word in longest_diverse_words:
                    continue
                if len(longest_diverse_words) < 10:
                    longest_diverse_words.append(word)
                else:
                    longest_diverse_words = sorted(longest_diverse_words, key=lambda x: len(set(x)))
                    if len(set(longest_diverse_words[0])) < len(set(word)):
                        longest_diverse_words[0] = word
    return longest_diverse_words


def get_rarest_char(file_path: str) -> str:
    chars_count = Counter()
    with open(file_path) as f:
        for line in f:
            data = line.strip().encode().decode('unicode-escape').lower().replace(' ', '')
            for char in data:
                if char not in chars_count:
                    chars_count[char] = 1
                else:
                    chars_count[char] += 1
    return chars_count.most_common()[-1][0]


def count_punctuation_chars(file_path: str) -> int:
    count = 0
    with open(file_path) as f:
        for line in f:
            data = line.strip().encode().decode('unicode-escape')
            for symbol in data:
                if symbol in string.punctuation:
                    count += 1
    return count


def count_non_ascii_chars(file_path: str) -> int:
    count = 0
    with open(file_path) as f:
        for line in f:
            data = line.strip().encode().decode('unicode-escape').strip()
            for element in data:
                if not element.isascii():
                    count += 1
    return count


def get_most_common_non_ascii_char(file_path: str) -> str:
    symbols = Counter()
    with open(file_path) as f:
        for line in f:
            data = line.strip().encode().decode('unicode-escape').strip()
            for element in data:
                if not element.isascii():
                    if element not in symbols:
                        symbols[element] = 1
                    else:
                        symbols[element] += 1
    return symbols.most_common(1)[0][0]
