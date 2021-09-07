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
    min_elem = None
    max_elem = None
    with open(file_name) as f:
        for line in f:
            split = [int(i) for i in line.strip().split()]
            min_in_split = min(split)
            max_in_split = max(split)
            if min_elem is None and max_elem is None:
                min_elem = min_in_split
                max_elem = max_in_split
            elif min_elem > min_in_split:
                min_elem = min_in_split
            elif max_elem < max_in_split:
                max_elem = max_in_split
    return min_elem, max_elem
