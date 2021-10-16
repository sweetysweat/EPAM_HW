import pytest

from homework9.hw_9_task_2 import ErrorHandler, error_handler


def test_func_error_handler_positive_case():
    with error_handler(IndexError):
        [][2]
    assert True


@pytest.mark.xfail
def test_func_error_handler_negative_case():
    with error_handler(ValueError):
        [][2]


@pytest.mark.xfail
def test_class_error_handler_negative_case():
    with error_handler(ZeroDivisionError):
        [][2]


def test_class_error_handler_positive_case():
    with ErrorHandler(IndexError):
        [][2]
    assert True
