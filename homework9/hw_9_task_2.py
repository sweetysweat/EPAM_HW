"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:

>> universal_file_counter(test_dir, "txt")
6
>> universal_file_counter(test_dir, "txt", str.split)
6
"""
import os
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None) -> int:
    count = 0
    for file_name in os.listdir(dir_path):
        if file_name.endswith(file_extension):
            if tokenizer:
                with open(file_name, 'r') as f:
                    for line in f:
                        count += len(tokenizer(line))
            else:
                with open(file_name, 'r') as f:
                    for _ in f:
                        count += 1
    return count
