from collections import Iterable

import homework3.task3 as t3


def test_if_Filter_gets_not_iterable_value():
    """
    Если мы создаем экземпляр класса Fileter с не итерируемым аргументом, то
    выполнение кода не является возможным.
    """
    var = t3.Filter(lambda x: x % 2 == 0)
    assert not isinstance(var, Iterable)


def test_if_filter_funcs_in_make_filter_create_not_iterable_value():
    """
        При вызове функции make_filter у нас должен создаваться итерируемый фильтр,
        но вместо этого в список кладутся ссылки на участок памяти, где хранится
        функция keyword_filter_func.
    """
    result = t3.make_filter(name='polly', type='bird')
    assert not isinstance(result, Iterable)
