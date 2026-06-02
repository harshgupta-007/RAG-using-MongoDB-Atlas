from src.generation.gemini_generator import (
    GeminiGenerator
)


class ChatTitleGenerator:

    def __init__(self):

        self.gemini = (
            GeminiGenerator()
        )

    def generate(
        self,
        first_message
    ):

        prompt = f"""
Generate a short chat title.

Rules:
- Maximum 5 words
- No quotes
- No punctuation
- Return title only

User Message:
{first_message}
"""

        title = (
            self.gemini.generate(
                prompt
            )
        )

        return (
            title
            .strip()
            .replace('"', '')
            .replace("\n", "")
        )