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

        return QueryIntent(
            **result
        )