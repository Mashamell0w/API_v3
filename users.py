import sqlite3
from flask_restful import reqparse, abort, Api, Resource

users = [
    {
        'user_name': 'Carl',
        'password': 'AbC12345'
    }
]


class User(object):
    def __init__(self, _id, user_name, password):
        self.id = _id
        self.user_name = user_name
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

    @staticmethod
    def find_by_user_name(name):
        con = sqlite3.connect('data.db')
        cur = con.cursor()

        query = 'SELECT * FROM users WHERE user_name=?'
        row = cur.execute(query, (name,)).fetchone()

        con.close()

        user = User(*row) if row else None
        return user

    @staticmethod
    def find_by_id(_id):
        con = sqlite3.connect('data.db')
        cur = con.cursor()

        query = 'SELECT * FROM users WHERE id=?'
        row = cur.execute(query, (_id,)).fetchone()

        con.close()

        user = User(*row) if row else None
        return user


class UserRegister(Resource):
    parser_item = reqparse.RequestParser()
    parser_item.add_argument('password')

    def post(self, user_name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        args = self.parser_item.parse_args()

        user = (user_name, args['password'])
        create_user = 'INSERT INTO users VALUES (NULL, ?, ?)'
        cursor.execute(create_user, user)

        connection.commit()
        connection.close()
        return {}
