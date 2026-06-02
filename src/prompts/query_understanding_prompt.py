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

Important:
If a field is unknown, return null.
Never return empty strings.

User Query:
{query}
"""