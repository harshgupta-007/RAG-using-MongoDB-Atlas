QUERY_UNDERSTANDING_PROMPT = """
You are a query understanding engine.

Extract:

- intent
- chapter
- section
- page_start
- page_end
- search_query

Return ONLY valid JSON.

User Query:
{query}
"""