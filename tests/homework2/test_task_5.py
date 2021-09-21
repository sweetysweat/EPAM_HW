import string

import pytest

from homework2.task5 import custom_range

"""3 param"""


@pytest.mark.parametrize("iter_item, first_token, second_token, step, expected", [
    [string.ascii_lowercase, 'p', 'g', -2, ['p', 'n', 'l', 'j', 'h']]
])
def test_custom_range_3_param(iter_item, first_token, second_token, step, expected):
    assert custom_range(iter_item, first_token, second_token, step) == expected


"""2 param"""


@pytest.mark.parametrize("iter_item, first_token, second_token, expected", [
    [string.ascii_lowercase, 'g', 'p', ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']]
])
def test_custom_range_two_param(iter_item, first_token, second_token, expected):
    assert custom_range(iter_item, first_token, second_token) == expected


"""1 param"""


@pytest.mark.parametrize("iter_item, first_token, expected", [
    [string.ascii_lowercase, 'g', ['a', 'b', 'c', 'd', 'e', 'f']]
])
def test_custom_range_one_param(iter_item, first_token, expected):
    assert custom_range(iter_item, first_token) == expected
