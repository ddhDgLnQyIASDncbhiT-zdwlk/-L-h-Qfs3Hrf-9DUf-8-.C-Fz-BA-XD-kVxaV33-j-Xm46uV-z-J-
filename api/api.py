from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import json  
import pymysql

# Connect to database
database = pymysql.connect(host='149.28.72.58', user='nkomarn', password='somepassoword', db='blaze', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

app = Flask(__name__)
api = Api(app)

class Cards(Resource):
    def get(self):
        with database.cursor() as cursor:
            cursor.execute("SELECT * FROM `cards`")
            return cursor.fetchall(), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True, help="Missing name.")
        parser.add_argument("description", required=True, help="Missing description.")
        args = parser.parse_args()

        with database.cursor() as cursor:
            cursor.execute("INSERT INTO `cards`(`name`, `description`) VALUES ('" + args['name'] + "', '" + args['description'] + "')")

class Messages(Resource):
    def get(self):
        try:
            with database.cursor() as cursor:
                cursor.execute("SELECT * FROM `messages`")
                return cursor.fetchall(), 200
        except:
            return "Database error.", 400


api.add_resource(Cards, '/cards')
api.add_resource(Messages, '/api/v1/user/messages')

if __name__ == '__main__':
    app.run(port='5050', debug=True)

"""
try:
    with database.cursor() as cursor:
        sql =
        cursor.execute(sql)
        result = cursor.fetchall()
        print (result)
finally:
    database.close()
"""