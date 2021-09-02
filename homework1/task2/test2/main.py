from task1.check_fibonachi import *


def test_fib():
    assert check_fibonacci([[]])
    assert check_fibonacci([[1]])
    assert check_fibonacci([[2]])
    assert check_fibonacci([[0, 1, 1, 2]])
