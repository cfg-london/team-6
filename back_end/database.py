import sqlite3
from laureate_class import Laureate
from caller import Caller

connection = sqlite3.connect("database.db")

cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS laureates (
  id int,
  poo bit,
  image_link VARCHAR(30), 
  wiki_link VARCHAR(30), 
  prize_list VARCHAR(30),
  firstname VARCHAR(30), 
  surname VARCHAR(30), 
  dob DATE, 
  dod DATE, 
  gender int,
  born_city VARCHAR(30),
  born_country VARCHAR(30), 
  organisation VARCHAR(30),
  description VARCHAR(30));""")

api = Caller()
api.initialize_prize_pool()

for id, laureate in api.laureate_pool.items():
  cursor.execute("INSERT INTO laureates VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (laureate.id, 1, laureate.image_link, laureate.wiki_link, str(laureate.prize_list), laureate.firstname, laureate.surname, laureate.dob, laureate.dod, laureate.gender, laureate.born_city, laureate.born_country, None, laureate.description))


#name = "albert"

#statement = "select * from laureates where firstname = \"" + name + "\""
#cursor.execute(statement)

print (cursor.fetchall())
connection.commit()
connection.close()
