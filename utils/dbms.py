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
        #cursor.execute(create_table_users)
        #cursor = conn.cursor()
        #create_table
        #create_table_queue =