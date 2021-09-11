import pytest
from homework2.task1 import get_longest_diverse_words, get_most_common_non_ascii_char, get_rarest_char
from homework2.task1 import count_punctuation_chars, count_non_ascii_chars


@pytest.mark.parametrize("test_input, expected", [['test_data.txt',
                                                   ['bedenklider', 'bedenklichen', 'bedenklileser', 'hinausführen',
                                                    'vorgebahnte', 'bedenkliauf', 'bedenklisich', 'bedenklimuß',
                                                    'hinbetrachtung', 'bedenklivielmehr']
                                                   ]]
                         )
def test_get_longest_diverse_words(test_input, expected):
    assert get_longest_diverse_words(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [['test_data.txt', 'ü']])
def test_get_most_common_non_ascii_char(test_input, expected):
    assert get_most_common_non_ascii_char(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [['test_data.txt', 'z']])
def test_get_rarest_char(test_input, expected):
    assert get_rarest_char(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [['test_data.txt', 7]])
def test_count_punctuation_chars(test_input, expected):
    assert count_punctuation_chars(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [['test_data.txt', 6]])
def test_count_non_ascii_chars(test_input, expected):
    assert count_non_ascii_chars(test_input) == expected
