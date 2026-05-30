import json

from src.database.collections import (
    parent_collection,
    child_collection
)


class MongoDBIngestion:

    def load_json(
        self,
        path
    ):

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)
        

    def ingest_parents(
        self,
        path
    ):

        docs = self.load_json(path)

        records = []

        for doc in docs:

            records.append({

                "_id":
                    doc["parent_id"],

                "text":
                    doc["text"],

                "metadata":
                    doc["metadata"]
            })

        parent_collection.delete_many({})

        result = parent_collection.insert_many(
            records
        )

        print(
            f"Inserted {len(result.inserted_ids)} parents"
        )

    def ingest_children(
        self,
        path
    ):

        docs = self.load_json(path)

        records = []

        for doc in docs:

            records.append({

                "_id":
                    doc["chunk_id"],

                "parent_id":
                    doc["parent_id"],

                "chunk_text":
                    doc["chunk_text"],

                "metadata":
                    doc["metadata"],

                "embedding":
                    doc["embedding"]
            })

        child_collection.delete_many({})

        result = child_collection.insert_many(
            records
        )

        print(
            f"Inserted {len(result.inserted_ids)} chunks"
        )