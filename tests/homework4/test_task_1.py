from homework4.task1 import read_magic_number
import os
import pytest


txt_file = "test_input_data.txt"


@pytest.fixture
def input_test_data():
    def write_into_file(data):
        with open(txt_file, 'w') as f:
            f.write(data)
        return
    yield write_into_file
    os.remove(txt_file)


@pytest.mark.parametrize("test_input", ['2'])
def test_read_magic_number_positive_case(test_input, input_test_data):
    input_test_data(test_input)
    assert read_magic_number(txt_file)


@pytest.mark.parametrize("test_input", ['0'])
def test_read_magic_number_negative_case(test_input, input_test_data):
    input_test_data(test_input)
    assert not read_magic_number("test_input_data.txt")


@pytest.mark.parametrize("test_input", ['qwe'])
def test_value_exception_in_read_magic_number(test_input, input_test_data):
    input_test_data(test_input)
    pytest.raises(ValueError, read_magic_number, "test_input_data.txt")
