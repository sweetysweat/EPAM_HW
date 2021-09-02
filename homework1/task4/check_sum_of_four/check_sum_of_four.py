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


print(check_sum_of_four([1, 0, 3], [1, 1, 0], [0, 1, 1], [0, 2, 3]))
