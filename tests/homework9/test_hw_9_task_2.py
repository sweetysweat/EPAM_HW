import os

import pytest

from homework9.hw_9_task_2 import universal_file_counter

directory = os.path.join(os.path.dirname(__file__))
file1 = os.path.join(os.path.dirname(__file__), "data1.txt")
file2 = os.path.join(os.path.dirname(__file__), "data2.txt")
file3 = os.path.join(os.path.dirname(__file__), "data3.md")


@pytest.fixture(autouse=True)
def write_into_file():
    with open(file1, 'w') as f:
        f.writelines(["1\n", "5\n", "7"])
    with open(file2, 'w') as f:
        f.writelines(["2\n", "4\n", "3"])
    with open(file3, 'w') as f:
        f.writelines(["Может быть тебе дать еще ключ от квартиры\n", "где деньги лежат"])
    yield
    os.remove(file1)
    os.remove(file2)
    os.remove(file3)


def test_universal_file_counter(write_into_file):
    assert universal_file_counter(directory, "txt") == 6
    assert universal_file_counter(directory, "md", str.split) == 11
