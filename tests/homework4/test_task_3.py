from homework4.task3 import my_precious_logger
import pytest


@pytest.mark.parametrize("test_input", ['qwe'])
def test_std_out_from_my_precious_logger(test_input, capsys):
    my_precious_logger(test_input)
    captured = capsys.readouterr()
    assert captured.out == test_input


@pytest.mark.parametrize("test_input", ['error: something bad'])
def test_std_err_from_my_precious_logger(test_input, capsys):
    my_precious_logger(test_input)
    captured = capsys.readouterr()
    assert captured.err == test_input

