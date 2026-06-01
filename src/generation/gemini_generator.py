from google import genai

from src.config.settings import settings
from src.prompts.rag_prompt import RAG_PROMPT


class GeminiGenerator:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate_answer(
        self,
        question,
        context
    ):

        prompt = RAG_PROMPT.format(
            context=context,
            question=question
        )

        response = self.client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        return response.text