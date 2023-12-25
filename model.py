import sqlite3
import re
import record as rd
from contextlib import closing

# way to input diff categories
# way to visualize
# way to track server job
# create $ per hour
# way to show best days to work
# spend vs profit


def database_handling(adding, record):
    try:
        with closing(sqlite3.connect('finance.db')) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS records (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        category TEXT NOT NULL,
                        price NUMERIC NOT NULL,
                        time TEXT NOT NULL
                    )
                ''')
                if adding:
                    cursor.execute(
                        'INSERT INTO records (name, category, price, time) VALUES (?, ?, ?, ?)',
                        (record.name, record.category, record.price, record.time)
                    )
                else:
                    cursor.execute(
                        'DELETE FROM records WHERE name = ? AND time = ?',
                        (record.name, record.time,)
                    )
    except sqlite3.Error as e:
        raise NameError()


def add(name, category, price):
    record = rd.Records(name, category, price)
    if price_validity(price) and database_handling(True, record):
        return True
    else:
        return False


def delete(name, category, price):
    try:
        record = rd.Records(name, category, price)
        database_handling(False, record)
        return True
    except NameError as e:
        return False


def price_validity(p):
    regex = r'^\d{1,3}(?:,?\d{3})*(?:\.\d{2})?$'
    if re.match(regex, p):
        return True
    else:
        return False
