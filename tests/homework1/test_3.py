import pytest
from homework1.task3 import find_maximum_and_minimum


@pytest.mark.parametrize("test_input, expectation", [['file.txt', (-1, 20)]])
def test_find_max_and_min(test_input, expectation):
    assert find_maximum_and_minimum(test_input) == expectation
