import sqlite3
import record as rd
from contextlib import closing

# way to input diff categories
# way to visualize
# way to track server job
# create $ per hour
# way to show best days to work
# spend vs profit

def database_handling(adding, record):
    with closing(sqlite3.connect('finance.db')) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS records (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL
                    category TEXT NOT NULL
                    price NUMERIC NOT NULL
                    time TEXT NOT NULL
                )
            ''')
            if adding:
                cursor.execute(
                    f'INSERT INTO records (id, name, category, price, time) VALUES '
                    f'({record.name}, {record.category}, {record.price}, {record.time}'
                )
            else:
                cursor.execute(
                    'DELETE FROM records WHERE name = ?, time = ?', (record.name, record.time,)
                )


def add():
    pass


def delete():
    pass
