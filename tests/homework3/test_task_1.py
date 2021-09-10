import unittest.mock

import pytest
from unittest.mock import patch
from homework3.task1 import f, fun


@pytest.mark.parametrize("test_input ,expectation", [[[2, 2], [16, 16, 16]]])
def test_fun(test_input, expectation):
    a = [fun(*test_input), fun(*test_input), fun(*test_input)]
    assert a == expectation


@patch('builtins.input', lambda: 1)
def test_f1():
    with unittest.mock.patch('builtins.input', return_value=1):
        a = [f(), f(), f()]
        assert a == [1, 1, 1]
