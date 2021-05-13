import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

query = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)'
cursor.execute(query)

create_user = 'INSERT INTO users VALUES (?, ?, ?)'
user = (1, 'anatolii', '123')
cursor.execute(create_user, user)

users = [
    (2, 'masha', '456'),
    (3, 'dasha', 'qwe')
]
cursor.executemany(create_user, users)

query = 'CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, item_name text, price int)'
cursor.execute(query)

create_item = 'INSERT INTO items VALUES (?, ?, ?)'
item = (1, 'coco', 23)
cursor.execute(create_item, item)

items = [
    (2, 'banana', 47),
    (3, 'cookie', 36)
]
cursor.executemany(create_item, items)


for row in cursor.execute('SELECT * FROM users'):
    print(row)

connection.commit()
connection.close()
