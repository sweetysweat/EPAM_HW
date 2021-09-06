import pytest
from homework1.task2 import check_fibonacci


@pytest.mark.parametrize("test_input, expectation", [[[0, 1, 1, 2], True], [[2, 3, 4], False]])
def test_fib(test_input, expectation):
    assert check_fibonacci(test_input) == expectation
    assert check_fibonacci(test_input) == expectation
