"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    min_and_max = []
    with open(file_name) as f:
        for line in f:
            split = [int(i) for i in line.strip().split()]
            min_and_max.append(min(split))
            min_and_max.append(max(split))
    return min(min_and_max), max(min_and_max)
