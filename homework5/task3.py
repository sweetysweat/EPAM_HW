from typing import Callable


def wrapper(string_to_add):
    def add_string(func: Callable) -> Callable:
        def prefix(*args, **kwargs) -> str:
            return f"{string_to_add} {func(*args, **kwargs)}"
        return prefix
    return add_string


@wrapper("hehe")
def sum_of_2(a, b):
    return a + b
