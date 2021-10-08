"""
Write a wrapper class TableData for database table, that when initialized with database name and table acts
 as collection object (implements Collection protocol). Assume all data has unique values in 'name' column.
  So, if presidents = TableData(database_name='example.sqlite', table_name='presidents')

then
    len(presidents) will give current amount of rows in presidents table in database
    presidents['Yeltsin'] should return single data row for president with name Yeltsin
    'Yeltsin' in presidents should return if president with same name exists in table
    object implements iteration protocol. i.e. you could use it in for loops::
        for president in presidents:
        print(president['name'])
    all above mentioned calls should reflect most recent data. If data in table changed after you created collection
    instance, your calls should return updated data.
Avoid reading entire table into memory. When iterating through records, start reading the first record, then go to the
next one, until records are exhausted. When writing tests, it's not always necessary to mock database calls completely.
Use supplied example.sqlite file as database fixture file.
"""
import sqlite3
from typing import Union


class TableData:
    def __init__(self, database_name: str, table_name: str):
        self. table_name = table_name
        self.conn = sqlite3.connect(database_name).cursor()
        self.row_index = -1
        self.amount_of_rows = self.conn.execute(f"SELECT COUNT(*) FROM {self.table_name}").fetchone()[0]

    def __len__(self) -> int:
        return self.amount_of_rows

    def __getitem__(self, name: str) -> tuple[Union[str, int]]:
        return self.conn.execute(f"SELECT * FROM {self.table_name} WHERE name = '{name}'").fetchone()

    def __iter__(self):
        return self

    def __next__(self) -> tuple:
        if self.row_index >= self.amount_of_rows - 1:
            raise StopIteration
        self.row_index += 1
        return self.conn.execute(f"SELECT * FROM {self.table_name}").fetchall()[self.row_index]
