from homework4.task5 import fizzbuzz
import pytest


@pytest.mark.parametrize("input_data, expectation", [[5, ["1", "2", "fizz", "4", "buzz"]]])
def test_fizzbuzz(input_data, expectation):
    assert [i for i in fizzbuzz(input_data)] == expectation
