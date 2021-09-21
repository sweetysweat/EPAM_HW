"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import List, Iterable, Any


def custom_range(iterable: Iterable, start, stop=None, step=1) -> List[Any]:
    result = []
    start = iterable.index(start)
    if stop is None:
        for i in range(0, start, step):
            result.append(iterable[i])
        return result
    else:
        stop = iterable.index(stop)
        for i in range(start, stop, step):
            result.append(iterable[i])
        return result
