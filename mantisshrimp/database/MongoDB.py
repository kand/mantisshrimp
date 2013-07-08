from pymongo import MongoClient

# TODO : replace stuff with app settings

connection = MongoClient('localhost', 27017)
database = connection['mantisshrimp_testing']
