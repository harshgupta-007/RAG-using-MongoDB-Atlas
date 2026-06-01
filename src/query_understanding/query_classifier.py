class QueryClassifier:

    def classify(
        self,
        query: str
    ):

        query = query.lower()

        if "chapter" in query:
            return "metadata"

        if "section" in query:
            return "metadata"

        if "page" in query:
            return "metadata"

        return "semantic"