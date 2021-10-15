import os

import pytest

from homework9.hw_9_task_1 import merge_sorted_files


@pytest.fixture(autouse=True)
def write_into_file():
    with open("data1.txt", 'w') as f:
        f.writelines(["1\n", "5\n", "7"])
    with open("data2.txt", 'w') as f:
        f.writelines(["2\n", "4\n", "3"])
    with open("data3.txt", 'w') as f:
        f.writelines(["6\n", "9\n", "8"])
    yield
    os.remove("data1.txt")
    os.remove("data2.txt")
    os.remove("data3.txt")


def test_merge_sorted_files(write_into_file):
    data = []
    for num in merge_sorted_files(["data1.txt", "data2.txt", "data3.txt"]):
        data.append(num)
    assert data == [1, 2, 3, 4, 5, 6, 7, 8, 9]
