class ContextBuilder:

    def build_context(
        self,
        parent_documents,
        max_documents=3
    ):

        selected_docs = (
            parent_documents[:max_documents]
        )

        context_sections = []

        for doc in selected_docs:

            chapter = (
                doc["metadata"]
                .get("chapter", "")
            )

            section = (
                doc["metadata"]
                .get("section", "")
            )

            match_count = (
                doc.get(
                    "match_count",
                    0
                )
            )

            context_sections.append(
                f"""
DOCUMENT ID: {doc['_id']}

MATCH COUNT: {match_count}

CHAPTER: {chapter}

SECTION: {section}

CONTENT:
{doc['text']}
"""
            )

        return "\n\n".join(
            context_sections
        )