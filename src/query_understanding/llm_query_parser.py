import json

from google import genai

from src.config.settings import settings

from src.prompts.query_understanding_prompt import (
    QUERY_UNDERSTANDING_PROMPT
)

from src.models.query_intent import (
    QueryIntent
)

class LLMQueryParser:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def parse(
        self,
        query
    ):

        prompt = QUERY_UNDERSTANDING_PROMPT.format(
            query=query
        )

        response = self.client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
)

        result = json.loads(
            response.text
        )

        response_json = json.loads(
            response.text
        )

        # -----------------------------
        # Normalize Empty Values
        # -----------------------------

        for field in [
            "chapter",
            "section",
            "search_query"
        ]:

            if response_json.get(field) == "":
                response_json[field] = None

        for field in [
            "page_start",
            "page_end"
        ]:

            if response_json.get(field) in ["", None]:
                response_json[field] = None

        response_json.setdefault(
    "search_query",
    query
)

        if not response_json.get(
            "search_query"
        ):
            response_json[
                "search_query"
            ] = query
        # print("\nRAW LLM RESPONSE")
        # print(response_json)
        return QueryIntent(
            **response_json
        )
