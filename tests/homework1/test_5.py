import pytest

from homework1.task5 import find_maximal_subarray_sum


@pytest.mark.parametrize("test_input, sub_len, expectation", [[[1, 3, -1, -3, 5, 3, 6, 7], 3, 16]])
def test_find_maximal_subarray_sum(test_input, sub_len, expectation):
    assert find_maximal_subarray_sum(test_input, sub_len) == expectation
