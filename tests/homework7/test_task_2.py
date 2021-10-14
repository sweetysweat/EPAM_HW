import pytest

from homework7.task_2 import backspace_compare

data_for_positive_tests = [["ad#c", "ad#c"], ["a##c", "#a#c"]]
data_for_negative_tests = [["a#c", "b"]]


@pytest.mark.parametrize("first_string, second_string", [*data_for_positive_tests])
def test_positive_backspace_compare(first_string, second_string):
    assert backspace_compare(first_string, second_string)


@pytest.mark.parametrize("first_string, second_string", [*data_for_negative_tests])
def test_negative_backspace_compare(first_string, second_string):
    assert not backspace_compare(first_string, second_string)
