import sqlite3
from flask_restful import reqparse, abort, Api, Resource


class Item(Resource):
    parser_item = reqparse.RequestParser()
    parser_item.add_argument('price', type=float)

    def get(self, item_name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM items WHERE item_name=?'
        row = cursor.execute(query, (item_name,)).fetchone()

        connection.close()

        item = Item(*row) if row else None
        connection.commit()
        connection.close()
        return item

    def post(self, item_name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        args = self.parser_item.parse_args()

        item = (item_name, args['password'])
        create_item = 'INSERT INTO items VALUES (NULL, ?, ?)'
        cursor.execute(create_item, item)

        connection.commit()
        connection.close()
        return {}

    def delete(self, name):
        for item in shop:
            if item['name'] == name:
                index = shop.index(item)
                del shop[index]
        return f'Item {name} was deleted'

    def put(self, name):
        if name not in [item['name'] for item in shop]:
            args = self.parser_item.parse_args()
            item = {'name': name, 'price': args['price']}
            shop.append(item)
            return item
        for item in shop:
            if item['name'] == name:
                args = self.parser_item.parse_args()
                item['price'] = args['price']
                return item


class ItemList(Resource):
    parser_shop = reqparse.RequestParser()
    parser_shop.add_argument('items', type=dict, action='append')

    def get(self):
        return {'items': shop}

    def post(self):
        args = self.parser_shop.parse_args()
        shop.extend(args['items'])
        return shop
