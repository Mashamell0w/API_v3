import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

connection.commit()
connection.close()
