import sqlite3
from multiprocessing import connection


def get_connection():
    try:
        con = sqlite3.connect("employee.db")
        cursor =connection.cursor()
        create_table_query=""""
        CREATE TABLE IF NOT EXISTS employee (
        id INTEGER NOT NULL PRIMARY KEY ,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        salary INTEGER NOT NULL
        );
        """""
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
        return connection
    except Exception as e:
        print("database connected")
        print(e)
        return None

