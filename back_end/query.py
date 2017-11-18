from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonpify

db_connect = create_engine('sqlite:///test.db')
app = Flask(__name__)
api = Api(app)

class Laureates(Resource):
  def get(self):
    conn = db_connect.connect()
    query = conn.execute("select * from laureates")
    return {'laureates' : [i for i in query.cursor.fetchall()]}

class First_Name(Resource):
  def get(self, first_name):
    conn = db_connect.connect()
    statement = "select * from laureates where firstname = \"" + first_name + "\""
    query = conn.execute(statement)
    return {first_name : [i for i in query.cursor.fetchall()]}


api.add_resource(Laureates, '/laureates')
api.add_resource(First_Name, '/first_name/<first_name>')

if __name__ == '__main__':
  app.run(port='5002')
