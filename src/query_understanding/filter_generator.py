class FilterGenerator:

    def generate(
        self,
        query_intent
    ):

        filters = {}

        if query_intent.chapter:

            filters[
                "metadata.chapter_number"
            ] = int(
                query_intent.chapter
            )

        return filters