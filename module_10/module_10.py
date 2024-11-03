import json
import os
import sqlite3
from module_6.task_6 import get_records_to_export, get_file_path

DB_NAME = 'test.db'
TABLE_NEWS = 'record_news'
TABLE_WEATHER = 'record_weather'
TABLE_AD = 'record_private_ad'


def is_table_exist(table_name):
    cursor.execute("""
        SELECT name 
        FROM sqlite_master 
        WHERE type='table' AND name=?;
    """, (table_name,))
    return cursor.fetchone() is not None


def init_table(table_name):
    if not is_table_exist(table_name):
        cursor.execute(f"CREATE TABLE {table_name} (text, unique_part)")


def get_table_by_record(_record):
    if _record['type'] == 'News':
        return TABLE_NEWS
    elif _record['type'] == 'Private Ad':
        return TABLE_AD
    elif _record['type'] == 'Weather':
        return TABLE_WEATHER

def is_duplicated(_table_name, _record):
    query = f"""
            SELECT * 
            FROM {_table_name} 
            WHERE text = ? AND unique_part = ?"""
    cursor.execute(query, (_record['text'], _record['unique_part']))
    result = cursor.fetchone()
    return result is not None

def insert_record(_record):
    table_name = get_table_by_record(_record)
    if not is_duplicated(table_name, _record):
        print(f"Inserting record {_record}")
        query = f"INSERT INTO {table_name} (text, unique_part) VALUES (?, ?)"
        cursor.execute(query, (_record['text'], _record['unique_part']))
        connection.commit()

def init_db(db_name):
    _connection = sqlite3.connect(db_name)
    _cursor = _connection.cursor()
    return _connection, _cursor

def close_db():
    cursor.close()
    connection.close()

if __name__ == '__main__':
    while True:
        print('-------------------')
        count = get_records_to_export()
        if count == 0:
            continue

        file_path = get_file_path('feed.json')
        if file_path is None:
            continue

        print(f"Opening the file: {file_path}")
        json_file = json.load(open(file_path))
        if count > len(json_file):
            print(f"Selected file contains only {len(json_file)} records. Please try again")
            continue

        print('Writing data into DB')
        connection, cursor = init_db(DB_NAME)
        init_table(TABLE_AD)
        init_table(TABLE_WEATHER)
        init_table(TABLE_NEWS)

        for i in range(0, count):
            insert_record(json_file[i])

        print('-------------------')
        print('Reading finished')
        print(f"Removing file {file_path}")
        os.remove(file_path)
        close_db()
