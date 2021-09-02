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
    print(find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3))
