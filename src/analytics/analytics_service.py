from src.database.collections import (
    retrieval_logs_collection
)


class AnalyticsService:

    def total_searches(
        self
    ):

        return (
            retrieval_logs_collection
            .count_documents({})
        )

    def avg_retrieval_time(
        self
    ):

        pipeline = [

            {
                "$group": {
                    "_id": None,
                    "avg_time": {
                        "$avg":
                        "$retrieval_time"
                    }
                }
            }
        ]

        result = list(
            retrieval_logs_collection.aggregate(
                pipeline
            )
        )

        if result:

            return round(
                result[0]["avg_time"],
                2
            )

        return 0

    def top_intents(
        self
    ):

        pipeline = [

            {
                "$group": {
                    "_id": "$intent",
                    "count": {
                        "$sum": 1
                    }
                }
            },

            {
                "$sort": {
                    "count": -1
                }
            }
        ]

        return list(
            retrieval_logs_collection.aggregate(
                pipeline
            )
        )

    def recent_searches(
        self,
        limit=20
    ):

        return list(

            retrieval_logs_collection
            .find()

            .sort(
                "created_at",
                -1
            )

            .limit(limit)
        )