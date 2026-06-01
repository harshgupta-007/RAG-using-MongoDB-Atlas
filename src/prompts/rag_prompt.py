RAG_PROMPT = """
You are an expert assistant.

Answer the user's question ONLY using the provided context.

If the answer is not available in the context, say:

"I could not find the answer in the retrieved documents."

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""