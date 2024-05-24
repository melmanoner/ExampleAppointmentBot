import sqlite3
from mysql.connector import Error

def create_tables():
    conn = sqlite3.connect('appointment.bd')
    try:
        cursor = conn.cursor()
        create_table_masters = '''
                CREATE TABLE IF NOT EXISTS masters(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                telephone TEXT,
                tg_id TEXT,
                earned TEXT
                )'''
        create_table_datetime = '''
                 CREATE TABLE IF NOT EXISTS datetime(
                 id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                 master_id INTEGER,
                 date TIMESTAMP,
                 time TEXT,
                 busy BOOLEAN,
                 FOREIGN KEY (master_id) REFERENCES masters(id)  ON DELETE CASCADE
                 )'''
        create_table_services = '''
                CREATE TABLE IF NOT EXISTS services(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price TEXT
                )'''
        create_table_users = '''
                CREATE TABLE IF NOT EXISTS users(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                tg_id INTEGER NOT NULL,
                username TEXT,
                first_name TEXT,
                date_reg TEXT
                )'''
        create_table_appointment = '''
                CREATE TABLE IF NOT EXISTS appointment(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                service_id INTEGER,
                master_id INTEGER,
                datetime_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES users(id)  ON DELETE CASCADE,
                FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE,
                FOREIGN KEY (master_id) REFERENCES masters(id) ON DELETE CASCADE,
                FOREIGN KEY (datetime_id) REFERENCES datetime(id) ON DELETE CASCADE
                )'''

        cursor.execute(create_table_masters)
        cursor.execute(create_table_users)
        cursor.execute(create_table_datetime)
        cursor.execute(create_table_services)
        cursor.execute(create_table_appointment)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

