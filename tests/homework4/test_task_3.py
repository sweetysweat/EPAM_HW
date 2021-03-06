import sys

import pytest

from homework4.task3 import my_precious_logger


@pytest.mark.parametrize("test_input", ["qwe", "error: something bad"])
def test_my_precious_logger(test_input, capsys):
    my_precious_logger(test_input)
    captured = capsys.readouterr()
    if sys.stderr.isatty():
        assert captured.err == test_input
    if sys.stdout.isatty():
        assert captured.out == test_input
