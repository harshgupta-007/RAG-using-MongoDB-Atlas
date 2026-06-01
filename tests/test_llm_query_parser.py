from src.query_understanding.llm_query_parser import (
    LLMQueryParser
)

parser = LLMQueryParser()

result = parser.parse(
    "Show aggregation examples from Chapter 6"
)

print(result)