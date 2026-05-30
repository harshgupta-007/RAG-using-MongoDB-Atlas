from pymongo import MongoClient

from src.config.settings import settings


class MongoDBClient:

    def __init__(self):

        self.client = MongoClient(
            settings.MONGO_URI
        )

        self.db = self.client[
            settings.DATABASE_NAME
        ]

    def get_database(self):

        return self.db