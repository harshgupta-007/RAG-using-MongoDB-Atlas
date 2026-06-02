from src.generation.chat_title_generator import (
    ChatTitleGenerator
)

generator = (
    ChatTitleGenerator()
)

title = (
    generator.generate(
        "Show aggregation examples from Chapter 6"
    )
)

print(title)