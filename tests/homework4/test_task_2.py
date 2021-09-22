import os
from contextlib import contextmanager
from unittest.mock import patch

from homework4.task2 import count_dots_on_i

path_to_test = os.getcwd() + "/tests/homework4/test_file.txt"


@contextmanager
def change_url_to_txt():
    f = open(path_to_test, 'rb')
    yield f.read().splitlines()
    f.close()


def test_count_dots_on_i():
    with patch("urllib.request.urlopen") as mock_urlopen:
        fake_page = change_url_to_txt()
        mock_urlopen.return_value = fake_page
        assert count_dots_on_i('any_text') == 59
