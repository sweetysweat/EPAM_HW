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


win_events = [[test_case_o_win_column, "o wins"], [test_case_o_win, "o wins"], [test_case_x_win, "x wins"]]
unfinished_and_draw_events = [[test_case_draw, "draw"], [test_case_unfinished_game, "unfinished"]]

all_events = win_events + unfinished_and_draw_events


@pytest.mark.parametrize("test_input, expectation", [*all_events])
def test_tic_tac_toe_checker_for_draw(test_input, expectation):
    assert tic_tac_toe_checker(test_input) == expectation
