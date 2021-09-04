import pytest
from homework1.task2 import check_fibonacci


@pytest.mark.parametrize("test_input", [[0, 1, 1, 2], [2, 3, 4]])
def test_fib(test_input):
    assert check_fibonacci(test_input)
    assert check_fibonacci(test_input)
