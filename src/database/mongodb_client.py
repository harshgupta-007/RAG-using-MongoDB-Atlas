from pymongo import MongoClient

from src.config.settings import settings


class MongoDBClient:

    def __init__(self):
        print("MONGO_URI exists:", bool(settings.MONGO_URI))
        print("MONGO_URI value:", repr(settings.MONGO_URI))

        self.client = MongoClient(
            settings.MONGO_URI
        )

        self.db = self.client[
            settings.DATABASE_NAME
        ]

    def get_database(self):

        return self.db