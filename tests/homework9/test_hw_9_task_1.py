import os

import pytest

from homework9.hw_9_task_1 import merge_sorted_files

txt_file1 = "data1.txt"
txt_file2 = "data2.txt"
txt_file3 = "data3.txt"


@pytest.fixture(autouse=True)
def write_into_file():
    with open(txt_file1, 'w') as f:
        f.writelines(["1\n", "5\n", "7"])
    with open(txt_file2, 'w') as f:
        f.writelines(["2\n", "4\n", "3"])
    with open(txt_file3, 'w') as f:
        f.writelines(["6\n", "9\n", "8"])
    yield
    os.remove(txt_file1)
    os.remove(txt_file2)
    os.remove(txt_file3)


def test_merge_sorted_files(write_into_file):
    data = []
    for num in merge_sorted_files([txt_file1, txt_file2, txt_file3]):
        data.append(num)
    assert data == [1, 2, 3, 4, 5, 6, 7, 8, 9]
