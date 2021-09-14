from homework4.task1 import read_magic_number
import os
import pytest


@pytest.mark.parametrize("test_input", ['2'])
def test_read_magic_number_positive_case(test_input):
    create_test_data(test_input)
    assert read_magic_number("test_input_data.txt")
    os.remove("test_input_data.txt")


@pytest.mark.parametrize("test_input", ['0'])
def test_read_magic_number_negative_case(test_input):
    create_test_data(test_input)
    assert not read_magic_number("test_input_data.txt")
    os.remove("test_input_data.txt")


def create_test_data(data):
    assert not os.path.isfile("test_input_data.txt")
    with open("test_input_data.txt", 'w') as f:
        f.write(data)


@pytest.mark.parametrize("test_input", ['qwe'])
def test_value_exception_in_read_magic_number(test_input):
    create_test_data(test_input)
    pytest.raises(ValueError, read_magic_number, "test_input_data.txt")
    os.remove("test_input_data.txt")


def check_that_there_is_no_created_data_for_test():
    return os.path.isfile("test_input_data")
