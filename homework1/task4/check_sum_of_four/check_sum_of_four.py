"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    length = len(a)
    count_zero = 0
    for a_counter in range(length):
        for b_counter in range(length):
            for c_counter in range(length):
                for d_counter in range(length):
                    if a[a_counter] + b[b_counter] + c[c_counter] + d[d_counter] == 0:
                        count_zero += 1
    return count_zero
