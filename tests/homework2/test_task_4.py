import pytest

from homework2.task4 import func


@pytest.mark.parametrize("test_input", [[100, 200]])
def test_cache(test_input):
    val_1 = func(*test_input)
    val_2 = func(*test_input)
    assert val_1 is val_2
