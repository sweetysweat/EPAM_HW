"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>> with supressor(IndexError):
...    [][2]
"""
from contextlib import contextmanager
from typing import Generator, Type


@contextmanager
def error_handler(*args: Type[Exception]) -> Generator:
    try:
        yield
    except args:
        pass


class ErrorHandler:
    def __init__(self, *args: Type[Exception]):
        self.error = args

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        return issubclass(exc_type, self.error)
