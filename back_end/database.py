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

p1 = Laureate(1, "a.com", "b.com", [1, 2, 3], "pordi", "jack", "1900-01-01", "2000-01-01", 2)

str_list = ''.join(str(e) for e in p1.prize_list)

cursor.execute("INSERT INTO laureate VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
(p1.id, 1, p1.image_link, p1.wiki_link, str_list, p1.entity.firstname, p1.entity.lastname, p1.entity.dob, p1.entity.dod, p1.entity.gender, None))

cursor.execute('SELECT * from laureate')

print (cursor.fetchall())

connection.commit()
connection.close()
