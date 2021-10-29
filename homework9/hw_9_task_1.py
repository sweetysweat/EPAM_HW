from contextlib import ExitStack
from heapq import merge
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    with ExitStack() as stack:
        files = [stack.enter_context(open(file_name)) for file_name in file_list]
        data = [[int(row) for row in file] for file in files]
        return iter(merge(*data))
