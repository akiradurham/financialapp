import sqlite3
import re
from contextlib import closing


def database_handling(adding, record):
    try:
        with closing(sqlite3.connect('finance.db')) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS serving (
                        id INTEGER PRIMARY KEY,
                        company TEXT NOT NULL,
                        hours TEXT NOT NULL,
                        profit NUMERIC NOT NULL,
                        date TEXT NOT NULL
                    )
                ''')
                if adding:
                    cursor.execute(
                        'INSERT INTO serving (company, hours, profit, date) VALUES (?, ?, ?, ?)',
                        (record.company.strip(), record.hours.strip(), record.profit.strip(), record.date.strip())
                    )
                else:
                    cursor.execute(
                        'DELETE FROM serving WHERE company = ? AND hours = ? AND profit = ? AND date = ?',
                        (record.company.strip(), record.hours.strip(), record.profit.strip(), record.date.strip())
                    )
                connection.commit()
    except Exception as e:
        raise NameError()


def add(record):
    if not price_validity(record.profit.strip()):
        return False
    if not inside(record):
        try:
            database_handling(True, record)
            return True
        except NameError as e:
            return False
    return False


def delete(record):
    if inside(record):
        try:
            database_handling(False, record)
            return True
        except NameError as e:
            return False
    else:
        return False


def inside(record):
    try:
        with closing(sqlite3.connect('finance.db')) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    'SELECT * FROM serving WHERE company = ? AND hours = ? AND profit = ? AND date = ?',
                    (record.company.strip(), record.hours.strip(), record.profit.strip(), record.date.strip())
                )
                return cursor.fetchall()
    except Exception as e:
        raise NameError()


def price_validity(p):
    regex = r'^\d{1,3}(?:,?\d{3})*(?:\.\d{2})?$'
    return re.match(regex, p)


def load_items():
    try:
        with closing(sqlite3.connect('finance.db')) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS serving (
                        id INTEGER PRIMARY KEY,
                        company TEXT NOT NULL,
                        hours TEXT NOT NULL,
                        profit NUMERIC NOT NULL,
                        date TEXT NOT NULL
                    )
                ''')
                cursor.execute(
                    'SELECT company, hours, profit, date FROM serving'
                )
                return cursor.fetchall()
    except Exception as e:
        raise NameError()
