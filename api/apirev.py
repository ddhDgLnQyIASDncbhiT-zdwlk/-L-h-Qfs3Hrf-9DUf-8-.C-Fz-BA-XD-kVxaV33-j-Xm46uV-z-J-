from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import json
import pymysql

apikey = "915ea4c1-bf7e-4038-97f8-047db982153f"

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# MySQL connection
try:
    print ('Attempting to connect to database...')
    database = pymysql.connect(host='149.28.72.58', user='nkomarn', password='somepassword', db='blaze', autocommit=True, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = database.cursor(pymysql.cursors.DictCursor)
except:
    print ('Cannot connect to database. Are the credentials correct?')
    exit()

            
class Messages(Resource):
    def get(self):
        with database.cursor() as cursor:
            cursor.execute("SELECT * FROM `messages`")
            return cursor.fetchall(), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("message", required=True)
        parser.add_argument("sender", required=True)
        parser.add_argument("recipient", required=True)
        parser.add_argument("time", required=True)
        args = parser.parse_args()

        with database.cursor() as cursor:
            cursor.execute("INSERT INTO `messages`(`sender`,`recipient`,`message`,`time`) VALUES ('" + args['sender'] + "','" + args['recipient'] + "','" + args['message'] + "','" + args['time'] + "')")
            return cursor.fetchall(), 200


class Cards(Resource):
    def get(self):
        with database.cursor() as cursor:
            cursor.execute("SELECT * FROM `cards`")
            data = cursor.fetchall()
            return data, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True, help="Missing name.")
        parser.add_argument("description", required=True, help="Missing description.")
        args = parser.parse_args()

        with database.cursor() as cursor:
            cursor.execute("INSERT INTO `cards`(`name`, `description`) VALUES ('" + args['name'] + "', '" + args['description'] + "')")

    #def delete(self, id):

api.add_resource(Messages, "/api/v1/user/messages")
api.add_resource(Cards, "/cards")
app.run(host='0.0.0.0')
crossdomain(origin='*')
