import unittest
from unittest.mock import patch

import pytest

from homework3.task1 import cache_factory, f, fun


def test_cache_factory_should_return_value_required_number_of_times():
    global test_data_for_cache_factory
    test_data_for_cache_factory = 0

    @cache_factory(3)
    def inner_test_func():
        global test_data_for_cache_factory
        test_data_for_cache_factory += 1
        return test_data_for_cache_factory

    for i in range(4):
        inner_test_func()

        """
        Значение глобальной переменной изменится только 1 раз, так как
        при первом вызове функции переменная увеличится на единицу, а в последующие
        2 раза значение возьмется из кеша. Поэтому только при четвертом вызове функции
        Значение увеличится на 1.
        """

    assert test_data_for_cache_factory == 2


@pytest.mark.parametrize("test_input", [[2, 2]])
def test_fun(test_input):
    a = [fun(*test_input), fun(*test_input), fun(*test_input)]
    assert a[0] is a[1] and a[0] is a[2]


@patch('builtins.input', lambda: 1)
def test_f1():
    with unittest.mock.patch('builtins.input', return_value=1):
        a = [f(), f(), f()]
        assert a[0] is a[1] and a[0] is a[2]
