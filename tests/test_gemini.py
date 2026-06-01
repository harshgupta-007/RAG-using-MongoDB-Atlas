from src.generation.gemini_generator import (
    GeminiGenerator
)

generator = GeminiGenerator()

response = generator.generate_answer(
    question="What is MongoDB?",
    context="MongoDB is a NoSQL database."
)

print(response)