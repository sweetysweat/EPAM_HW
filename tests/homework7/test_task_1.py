import pytest

from homework7.task_1 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
    },
    "fourth": "RED",
}


@pytest.mark.parametrize("test_input, element_to_find, expectation", [[example_tree, ["BLUE", "a", "RED"], [2, 1, 6]]])
def test_find_occurrences(test_input, element_to_find, expectation):
    for element, expect in zip(element_to_find, expectation):
        assert find_occurrences(test_input, element) == expect
