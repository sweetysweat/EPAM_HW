"""
In previous homework task 4, you wrote a cache function that remembers other function output value. Modify it to be a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass
Would give out cached value up to times number only. Example:

@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead

>> f()
? 1
'1'
>> f()     # will remember previous value
'1'
>>f()     # but use it up to two times only
'1'
>>f()
? 2
'2'

"""
from typing import Callable


def cache_factory(times=2):
    def cache(func: Callable) -> Callable:
        cached = {}

        def cash_data(*args):
            if args in cached:
                cached[args][1] -= 1
                if cached[args][1] == 0:
                    cached[args] = [func(*args), times]
                    return cached[args][0]
                return cached[args][0]
            cached[args] = [func(*args), times]
            return cached[args][0]

        return cash_data

    return cache


@cache_factory(times=3)
def fun(a, b):
    return (a ** b) ** 2


@cache_factory(times=3)
def f():
    return input('? ')
