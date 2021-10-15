from contextlib import ExitStack
from itertools import chain
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    with ExitStack() as stack:
        files = [stack.enter_context(open(file_name)) for file_name in file_list]
        data = [[int(num) for num in row] for row in zip(*files)]
        return chain.from_iterable(data)
