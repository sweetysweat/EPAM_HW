"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from itertools import chain
from typing import Any, List, Union


def check_row(row: List[Any]) -> Union[str, None]:
    row = set(row)
    if '-' not in row and len(row) == 1:
        return row.pop()


def check_winner_by_rows(board: List[Any]) -> Union[str, None]:
    for row_in_board in board:
        if check_row(row_in_board):
            return check_row(row_in_board)


def check_winner_by_columns(board: List[List]) -> Union[str, None]:
    new_board = list(zip(*board))
    return check_winner_by_rows(new_board)


def check_winner_by_left_diagonal(board: List[List]) -> Union[str, None]:
    diagonal = [board[i][i] for i in range(len(board))]
    return check_row(diagonal)


def check_winner_by_right_diagonal(board: List[List]) -> Union[str, None]:
    length = len(board)
    diagonal = [board[i][length - 1 - i] for i in range(length)]
    return check_row(diagonal)


def check_winner(board: List[List]) -> Union[str, None]:
    win_by_rows_or_columns = check_winner_by_rows(board) or check_winner_by_columns(board)
    win_by_diagonals = check_winner_by_left_diagonal(board) or check_winner_by_right_diagonal(board)
    return win_by_rows_or_columns or win_by_diagonals


def tic_tac_toe_checker(board: List[List]) -> str:
    find_winner = check_winner(board)
    if find_winner:
        return f"{find_winner} wins"
    elif '-' in chain.from_iterable(board):
        return "unfinished"
    else:
        return "draw"
