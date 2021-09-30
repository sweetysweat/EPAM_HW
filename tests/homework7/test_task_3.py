import pytest

from homework7.task_3 import tic_tac_toe_checker

test_case_x_win = [["-", "-", "o"],
                   ["-", "o", "o"],
                   ["x", "x", "x"]]

test_case_o_win = [["-", "-", "o"],
                   ["-", "o", "o"],
                   ["o", "x", "x"]]

test_case_o_win_column = [["-", "-", "o"],
                          ["x", "o", "o"],
                          ["x", "x", "o"]]

test_case_unfinished_game = [["-", "-", "o"],
                             ["-", "x", "o"],
                             ["x", "o", "x"]]

test_case_draw = [["o", "o", "x"],
                  ["x", "x", "o"],
                  ["o", "o", "x"]]


@pytest.mark.parametrize("test_input, expectation", [[test_case_draw, "draw"]])
def test_tic_tac_toe_checker_for_draw(test_input, expectation):
    assert tic_tac_toe_checker(test_input) == expectation


@pytest.mark.parametrize("test_input, expectation", [[test_case_unfinished_game, "unfinished"]])
def test_tic_tac_toe_checker_for_unfinished_game(test_input, expectation):
    assert tic_tac_toe_checker(test_input) == expectation


@pytest.mark.parametrize("test_input, expectation", [[test_case_x_win, "x wins"]])
def test_tic_tac_toe_checker_for_x_win(test_input, expectation):
    assert tic_tac_toe_checker(test_input) == expectation


@pytest.mark.parametrize("test_input, expectation", [[test_case_o_win, "o wins"]])
def test_tic_tac_toe_checker_for_o_win(test_input, expectation):
    assert tic_tac_toe_checker(test_input) == expectation


@pytest.mark.parametrize("test_input, expectation", [[test_case_o_win_column, "o wins"]])
def test_tic_tac_toe_checker_for_o_win_column(test_input, expectation):
    assert tic_tac_toe_checker(test_input) == expectation
