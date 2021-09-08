"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import List, Any
import string


def custom_range(iterable: Any, start, stop=None, step=1) -> List[Any]:
    lst = []
    start = iterable.index(start)
    if stop is None:
        for i in range(0, start, step):
            lst.append(iterable[i])
        return lst
    else:
        stop = iterable.index(stop)
        for i in range(start, stop, step):
            lst.append(iterable[i])
        return lst
