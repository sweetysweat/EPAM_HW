import pytest

from homework1.task1.sample_project.calculator.calc import check_power_of_2


@pytest.mark.parametrize("test_input, expectation", [[2, True], [1, True], [0, False], [65536, True], [12, False]])
def test_check_power_of_2(test_input, expectation):
    assert check_power_of_2(test_input) == expectation
