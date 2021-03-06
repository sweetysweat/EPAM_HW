"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""


def modify_string(input_string: str) -> str:
    modified_string = []
    for char in input_string:
        if char == "#" and modified_string:
            modified_string.pop()
        else:
            modified_string.append(char)
    return "".join(modified_string)


def backspace_compare(first: str, second: str) -> bool:
    return modify_string(first) == modify_string(second)
