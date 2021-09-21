import pytest

from homework1.task4 import check_sum_of_four


@pytest.mark.parametrize("a, b, c, d, expectation", [[[1, 0, 3], [1, 1, 0], [0, 1, 1], [0, 2, 3], 1]])
def test_check_sum_of_four(a, b, c, d, expectation):
    assert check_sum_of_four(a, b, c, d) == expectation
