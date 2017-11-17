import sqlite3
connection = sqlite3.connect("test.db")

sql_command = """
  CREATE TABLE IF NOT EXISTS laureate (
    first_name VARCHAR(10),
    last_name VARCHAR(10)
  );
"""
cursor = connection.cursor()
cursor.execute(sql_command)

sql_command = """INSERT INTO laureate (first_name, last_name)
  VALUES ("test_first_name", "test_last_name");"""

cursor.execute(sql_command)

cursor.execute('SELECT *')
cursor.close()
