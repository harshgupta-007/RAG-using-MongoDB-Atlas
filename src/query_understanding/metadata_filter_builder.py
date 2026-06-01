import re


class MetadataFilterBuilder:

    def build(
        self,
        query: str
    ):

        filters = {}

        chapter_match = re.search(
            r"chapter\s+(\d+)",
            query,
            re.IGNORECASE
        )

        if chapter_match:

            chapter_num = (
                chapter_match.group(1)
            )

            filters[
                "metadata.chapter"
            ] = {
                "$regex":
                f"Chapter {chapter_num}"
            }

        return filters
    


    