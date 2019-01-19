import pymongo


class Database(object):
    URI = "mongodb://127.0.0.1:27017" # the the databases we will create wi be go to same URI and same database that why
    DATABASE = None                   # we don't need __init__()

    @staticmethod  # because this method is not gonna instant of this class
    def initialize():  # in app.py file we first to initialize then its contain the database
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client["fullstack1"]

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
