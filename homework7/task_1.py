"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

counter = 0


def find_occurrences(tree: dict, element: Any) -> int:
    global counter
    if isinstance(tree, dict):
        for item in tree.values():
            find_occurrences(item, element)
    elif type(tree) in [set, list, tuple]:
        for item in tree:
            find_occurrences(item, element)
    elif tree == element:
        counter += 1
    return counter
