from pymongo import MongoClient


class MongoConnection:
    @staticmethod
    def create_connection():
        client = client = MongoClient("mongodb://root:senha123@localhost:27017")
        return client
    @staticmethod
    def create_dabase(client,name):
        db = client['name']
        return db