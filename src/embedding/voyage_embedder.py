import voyageai

from src.config.settings import settings


class VoyageEmbedder:

    def __init__(self):

        self.client = voyageai.Client(
            api_key=settings.VOYAGE_API_KEY
        )

    def embed_query(
        self,
        query
    ):

        result = self.client.embed(
            [query],
            model="voyage-3-large",
            input_type="query"
        )

        return result.embeddings[0]