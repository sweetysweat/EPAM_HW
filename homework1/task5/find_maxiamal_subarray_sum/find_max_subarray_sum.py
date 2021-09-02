"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_sum = 0
    sub_arr_sum = 0
    length = len(nums)
    for i in range(length):
        for j in range(k):
            if i + j >= length:
                break
            sub_arr_sum += nums[i+j]
            if sub_arr_sum > max_sum:
                max_sum = sub_arr_sum
        sub_arr_sum = 0
    return max_sum


if __name__ == '__main__':
    find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3)
