import sqlite3
from mysql.connector import Error

def create_tables():
    conn = sqlite3.connect('appointment.bd')
    try:
        cursor = conn.cursor()
        create_table_users = '''
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        tg_id INTEGER NOT NULL,
        username TEXT,
        first_name TEXT,
        date_reg TEXT
        )'''
        create_table_masters = '''
        CREATE TABLE IF NOT EXISTS masters(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        telephone TEXT,
        tg_id TEXT,
        earned TEXT)'''
        create_table_services = '''
        CREATE TABLE IF NOT EXISTS services(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price TEXT,
        master TEXT
        )'''

        cursor.execute(create_table_users)
        cursor.execute(create_table_masters)
        cursor.execute(create_table_services)
