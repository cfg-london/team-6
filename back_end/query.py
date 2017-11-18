from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonpify
from flask_cors import CORS, cross_origin
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


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
    def get(self, search_query, no_of_results):
        n_results = int(no_of_results)
        conn = db_connect.connect()
        all_laureates = conn.execute("select * from laureates")
        return_json = {}
        string_to_search = search_query.replace('%20', ' ')
        for l in all_laureates:
            d = dict(l.items())
            match_score = 0
            words = string_to_search.split(' ')
            for word in words:
                match_score += 70 * fuzz.ratio(word, d['firstname'].lower())
                match_score += 40 * fuzz.ratio(word, d['surname'].lower())
                match_score += fuzz.partial_ratio(search_query, d['description']) * d['description'].count(word)
                match_score += 3 * fuzz.ratio(search_query, d['dob'])
                match_score += 3 * fuzz.ratio(search_query, d['dod'])
                match_score += 3 * fuzz.partial_ratio(search_query, d['prize_list'])
                match_score += 5 * fuzz.ratio(search_query, d['born_city'])
                match_score += 3 * fuzz.ratio(search_query, d['born_country'])
                match_score += 20 * fuzz.partial_ratio(search_query, d['organisation'])
            return_json[match_score] = d
        return_entries = []
        for score, entry in reversed(sorted(return_json.items())):
            entry['score'] = score
            return_entries.append(entry)
        return return_entries[:n_results]
            

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
    return {'random' : [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}

class ID (Resource):
  def get(self, num):
    conn = db_connect.connect()
    statement = "select * from laureates where id = \"" + num + "\""
    query = conn.execute(statement)
    return {num : [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}

class Country (Resource):
  def get(self, born_country):
    conn = db_connect.connect()
    statement = "select * from laureates where lower(born_country) = \"" + born_country.lower() + "\"" 
    query = conn.execute(statement) 
    return {born_country : [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}

class Date_Of_Birth(Resource):
  def get(self, dob):
    conn = db_connect.connect()
    statement = "select * from laureates where dob = \"" + dob + "\"" 
    query = conn.execute(statement) 
    return {dob : [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}

class City(Resource):
  def get(self, born_city):
    conn = db_connect.connect()
    statement = "select * from laureates where lower(born_city) = \"" + born_city.lower() + "\"" 
    query = conn.execute(statement) 
    return {born_city : [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}


if __name__ == '__main__':
    db_connect = create_engine('sqlite:///database.db')
    app = Flask(__name__)
    CORS(app)
    api = Api(app)
    api.add_resource(Laureates, '/laureates')
    api.add_resource(First_Name, '/first_name/<first_name>')
    api.add_resource(Last_Name, '/last_name/<last_name>')
    api.add_resource(Full_Name, '/full_name/<full_name>')
    api.add_resource(GenericSearch, '/search/<search_query>/<no_of_results>')
    api.add_resource(Random, '/random/<number>')
    api.add_resource(ID, '/id/<num>')
    api.add_resource(Country, '/country/<born_country>')
    api.add_resource(Date_Of_Birth, '/date_of_birth/<dob>')
    api.add_resource(City, '/city/<born_city>')
    #CORS(api)
    app.run(host='0.0.0.0', port='5002')
    #conn = db_connect.connect()
    #all_laureates = conn.execute("select * from laureates")
    #return_json = {}
    #for l in all_laureates:
    #    d = dict(l.items())
    #    match_score = 0
    #    print(d['firstname'] + " " + str(fuzz.ratio('albert', d['firstname'].lower())))

