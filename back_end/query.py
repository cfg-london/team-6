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
    return {'laureates' : [i[0] for i in query.cursor.fetchall()]}

api.add_resource(Laureates, '/laureates')

if __name__ == '__main__':
  app.run(port='5002')
