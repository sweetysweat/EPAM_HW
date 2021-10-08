import os
from homework8.task_2 import TableData

data_base = os.getcwd() + "/tests/homework8/example.sqlite"

test_data = [('Yeltsin', 999, 'Russia'),
             ('Trump', 1337, 'US'),
             ('Big Man Tyrone', 101, 'Kekistan')]


def test_TableData():
    presidents = TableData(data_base, "presidents")
    assert len(presidents) == 3
    assert presidents['Trump'] == ('Trump', 1337, 'US')
    rows = []
    for element in presidents:
        rows.append(element)
    assert rows == test_data
