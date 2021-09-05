"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    max_elem, min_elem = 0, 0
    dic = {}
    lst = []
    for num in inp:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
    for element in dic:
        lst.append(dic[element])
    most = max(lst)
    least = min(lst)
    for key, value in dic.items():
        if dic[key] == most:
            max_elem = key
        elif dic[key] == least:
            min_elem = key
    return max_elem, min_elem
