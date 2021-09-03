import pytest
from calculator.calc import check_power_of_2


@pytest.mark.parametrize("test_input, expectation", [[2, True], [1, True], [0, False]])
def test_check_power_of_2(test_input, expectation):
    assert check_power_of_2(test_input) == expectation
    assert check_power_of_2(test_input) == expectation
    assert check_power_of_2(test_input) == expectation

