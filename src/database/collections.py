from src.database.mongodb_client import MongoDBClient
from src.config.settings import settings


client = MongoDBClient()

db = client.get_database()

parent_collection = db[
    settings.PARENT_COLLECTION
]

child_collection = db[
    settings.CHILD_COLLECTION
]