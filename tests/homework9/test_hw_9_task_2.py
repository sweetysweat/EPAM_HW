import pytest

from homework9.hw_9_task_2 import ErrorHandler, error_handler


@pytest.mark.parametrize("call_obj", [error_handler, ErrorHandler])
def test_func_and_class_error_handler_positive_case(call_obj):
    try:
        with call_obj(IndexError):
            [][2]
    except IndexError:
        pytest.fail("No exception was thrown")


@pytest.mark.parametrize("call_obj", [error_handler, ErrorHandler])
def test_func_and_class_error_handler_negative_case(call_obj):
    with pytest.raises(IndexError):
        with call_obj(ValueError):
            [][2]
