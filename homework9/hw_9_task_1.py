from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    data = []
    for file in file_list:
        with open(file, 'r') as f:
            for line in f:
                data.append(int(line.strip()))
    for num in sorted(data):
        yield num
