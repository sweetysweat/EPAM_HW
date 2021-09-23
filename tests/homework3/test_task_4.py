import pytest

from homework3.task4 import is_armstrong


@pytest.mark.parametrize("test_input", [9, 153])
def test_is_armstrong_for_positive_cases(test_input):
    assert is_armstrong(test_input)


@pytest.mark.parametrize("test_input", [12])
def test_is_armstrong_for_negative_cases(test_input):
    assert not is_armstrong(test_input)
