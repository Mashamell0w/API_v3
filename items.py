from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

shop = [
    {
        'name': 'banana',
        'price': 350
    },
    {
        'name': 'art',
        'price': 550
    }
]


def abort_if_item_doesnt_exist(name):
    if name not in [item['name'] for item in shop]:
        abort(404, message=f"Item {name} doesn't exist")


class Item(Resource):
    parser_item = reqparse.RequestParser()
    parser_item.add_argument('price', type=float)

    def get(self, name):
        abort_if_item_doesnt_exist(name)
        for item in shop:
            if item['name'] == name:
                index = shop.index(item)
                return shop[index]

    def post(self, name):
        args = self.parser_item.parse_args()
        item = {'name': name, 'price': args['price']}
        shop.append(item)
        return item

    def delete(self, name):
        abort_if_item_doesnt_exist(name)
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
