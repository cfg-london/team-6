import sqlite3
from laureate_class import Laureate
from caller import Caller

connection = sqlite3.connect("test.db")

cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS laureate (id int, poo bit, image_link VARCHAR(30), wiki_link VARCHAR(30), prize_list VARCHAR(30), first_name VARCHAR(30), last_name VARCHAR(30), dob DATE, dod DATE, gender int, organisation VARCHAR(30));")

api = Caller()
api.initialize_prize_pool()

for id, laureate in api.laureate_pool.items(): 
  str_list = ''.join(str(e) for e in laureate.prize_list)
  cursor.execute("INSERT INTO laureate VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (laureate.id, 1, laureate.image_link, laureate.wiki_link, str_list, laureate.firstname, laureate.surname, laureate.dob, laureate.dod, laureate.gender, None))

name = "pordi"

cursor.execute("SELECT * FROM laureate")

print (cursor.fetchall())
connection.commit()
connection.close()
