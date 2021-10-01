import pytest

from homework7.task_1 import find_occurrences

# Example tree:
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


@pytest.mark.parametrize("test_input, element_to_find, expectation", [[example_tree, "RED", 6]])
def test_find_occurrences_red(test_input, element_to_find, expectation):
    assert find_occurrences(test_input, element_to_find) == expectation


@pytest.mark.parametrize("test_input, element_to_find, expectation", [[example_tree, "a", 1]])
def test_find_occurrences_a(test_input, element_to_find, expectation):
    assert find_occurrences(test_input, element_to_find) == expectation


@pytest.mark.parametrize("test_input, element_to_find, expectation", [[example_tree, "BLUE", 2]])
def test_find_occurrences_blue(test_input, element_to_find, expectation):
    assert find_occurrences(test_input, element_to_find) == expectation
