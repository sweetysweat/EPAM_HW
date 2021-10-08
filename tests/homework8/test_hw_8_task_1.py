import os

import pytest

from homework8.task_1 import KeyValueStorage

txt_file = 'data.txt'


@pytest.fixture
def input_test_data():
    def write_into_file(data):
        with open(txt_file, 'w') as f:
            f.writelines(data)
        return

    yield write_into_file
    os.remove(txt_file)


data = ["name=kek\n", "last_name=top\n", "power=9001\n", "song=shadilay"]


def test_KeyValueStorage(input_test_data):
    input_test_data(data)
    storage = KeyValueStorage("data.txt")
    assert storage['name'] == "kek"
    assert storage.last_name == "top"
    assert storage.power == 9001
    assert storage.song == "shadilay"


@pytest.mark.parametrize("incorrect_data", ["1name=kek\n", "1=kek\n", "что-то=kek\n"])
def test_KeyValueStorage_with_incorrect_data(incorrect_data, input_test_data):
    input_test_data(incorrect_data)
    with pytest.raises(ValueError):
        KeyValueStorage("data.txt")
