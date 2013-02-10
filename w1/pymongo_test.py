import pymongo

from pymongo import Connection
connection = Connection('localhost', 27017)

db = connection.test

names = db.collect

items = names.find_one()

print items['name']
