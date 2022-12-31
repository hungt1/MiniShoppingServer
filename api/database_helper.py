import sqlite3
import os

def open_db(name):
    conn = sqlite3.connect(name)
    conn.row_factory = sqlite3.Row
    return conn

def copy_table(table_name, src, dest):
    if os.path.exists(dest):
        os.remove(dest)

    os.system("cp " + src + " " + dest)
    conn = open_db(dest)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        if table["name"] != table_name and table["name"] != "sqlite_sequence":
            cursor.execute("DROP TABLE " + table["name"])
    
    
    conn.commit()
    conn.close()