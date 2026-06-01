from src.query_understanding.llm_query_parser import (
    LLMQueryParser
)

from src.query_understanding.filter_generator import (
    FilterGenerator
)

query = (
    "Show aggregation examples from Chapter 6"
)

parser = LLMQueryParser()

intent = parser.parse(query)

generator = FilterGenerator()

filters = (
    generator.generate(intent)
)

print(filters)