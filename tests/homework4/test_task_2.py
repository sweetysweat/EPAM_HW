from contextlib import contextmanager
from unittest.mock import patch

from homework4.task2 import count_dots_on_i


@contextmanager
def change_url_to_txt():
    f = open('test_data_for_task_2.txt', 'rb')
    yield f.read().splitlines()
    f.close()


def test_count_dots_on_i():
    with patch("urllib.request.urlopen") as mock_urlopen:
        fake_page = change_url_to_txt()
        mock_urlopen.return_value = fake_page
        assert count_dots_on_i('any_text') == 59
