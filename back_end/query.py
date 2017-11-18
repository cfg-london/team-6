from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonpify
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

db_connect = create_engine('sqlite:///database.db')
app = Flask(__name__)
api = Api(app)

class Laureates(Resource):
  def get(self):
    conn = db_connect.connect()
    query = conn.execute("select * from laureates")
    return {'laureates' : [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}

class First_Name(Resource):
  def get(self, first_name):
    conn = db_connect.connect()
    statement = "select * from laureates where lower(firstname) = \"" + first_name.lower() + "\""
    query = conn.execute(statement)
    return {first_name : [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}

class Last_Name(Resource):
  def get(self, last_name):
    conn = db_connect.connect()
    statement = "select * from laureates where lower(surname) = \"" + last_name.lower() + "\""
    query = conn.execute(statement)
    return {last_name : [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}

class GenericSearch(Resource):
    def get(self, search_query):
        conn = db_connect.connect()
        all_laureates = conn.execute("select * from laureates")
        return_json = {}
        string_to_search = search_query.replace('_', ' ')
        for l in all_laureates:
            d = dict(l.items())
            match_score = 0
            match_score += 10 * fuzz.ratio(search_query, d['firstname'] + " " + d['surname'])
            match_score += fuzz.ratio(search_query, d['dob'])
            match_score += fuzz.ratio(search_query, d['dod'])
            match_score += fuzz.ratio(search_query, d['born_city'])
            match_score += fuzz.ratio(search_query, d['born_country'])
            match_score += fuzz.partial_ratio(search_query, d['organisation'])
            match_score += fuzz.partial_ratio(search_query, d['description'])
            return_json[match_score] = d
        return return_json
            

class Full_Name(Resource):
  def get(self, full_name):
    conn = db_connect.connect()
    name_list = full_name.split('%')
    first_name = name_list[0]
    last_name = name_list[1]  
    statement = "select * from laureates where lower(surname) = \"" + last_name.lower() + "\"" +"and lower(firstname) = \"" + first_name.lower() + "\""
    query = conn.execute(statement)
    return {full_name : [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}


class Random(Resource):
  def get(self, number):
    conn = db_connect.connect()
    statement = "SELECT * FROM laureates ORDER by RANDOM() LIMIT " + number
    query = conn.execute(statement)
    return {'Random' : [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}



api.add_resource(Laureates, '/laureates')
api.add_resource(First_Name, '/first_name/<first_name>')
api.add_resource(Last_Name, '/last_name/<last_name>')
api.add_resource(Full_Name, '/full_name/<full_name>')
api.add_resource(GenericSearch, '/search/<search_query>')
api.add_resource(Random, '/random/<number>')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='5002')
