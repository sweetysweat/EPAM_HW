import pytest
from homework2.task3 import combinations


@pytest.mark.parametrize("test_input, expected", [
                                                    [
                                                        [[1, 2], [3, 4]],
                                                        [[1, 3], [1, 4], [2, 3], [2, 4]]
                                                    ]
                                                ])
def test_combinations(test_input, expected):
    assert combinations(*test_input) == expected
