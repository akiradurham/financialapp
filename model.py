import sqlite3
import re
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
                        (record.name.strip(), record.category.strip(), record.price.strip(), record.time.strip())
                    )
                else:
                    cursor.execute(
                        'DELETE FROM records WHERE name = ? AND time = ?',
                        (record.name.strip(), record.time.strip(),)
                    )
    except Exception as e:
        raise NameError()


def add(record):
    if (record.name.strip() or record.category.strip() or record.price.strip() or record.time.strip()) == '':
        return False
    if not price_validity(record.price.strip()):
        return False
    try:
        database_handling(True, record)
        return True
    except NameError as e:
        return False


def delete(record):
    try:
        database_handling(False, record)
        return True
    except NameError as e:
        return False


def price_validity(p):
    regex = r'^\d{1,3}(?:,?\d{3})*(?:\.\d{2})?$'
    return re.match(regex, p)
