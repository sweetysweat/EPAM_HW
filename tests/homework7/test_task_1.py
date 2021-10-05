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
test_cases = [("BLUE", 2), ("a", 1), ("RED", 6)]


@pytest.mark.parametrize("element_to_find, expectation", test_cases)
def test_find_occurrences(element_to_find, expectation):
    assert find_occurrences(example_tree, element_to_find) == expectation
