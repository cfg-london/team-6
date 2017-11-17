import sqlite3
from laureate_class import Laureate

connection = sqlite3.connect("test.db")

sql_command = """
  CREATE TABLE IF NOT EXISTS laureate (
    id int,
    poo bit,
    image_link VARCHAR(30),
    wiki_link VARCHAR(30),
    prize_list VARCHAR(30),
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    dob DATE,
    dod DATE,
    gender int,
    organisation VARCHAR(30)
  );
"""
cursor = connection.cursor()
cursor.execute(sql_command)

cursor.execute(sql_command)

cursor.execute('SELECT * from laureate')

print (cursor.fetchall())

connection.commit()
connection.close()
