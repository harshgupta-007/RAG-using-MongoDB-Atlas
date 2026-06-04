import json

from google import genai
from pymongo import logger

from src.config.settings import settings

from src.prompts.query_understanding_prompt import (
    QUERY_UNDERSTANDING_PROMPT
)

from src.models.query_intent import (
    QueryIntent
)
from src.utils.logger import (
    logger
)
from src.utils.exceptions import (
    QueryParserError
)


# from google.genai.errors import ClientError
class LLMQueryParser:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def parse(
            self,
            query
        ):
            prompt = QUERY_UNDERSTANDING_PROMPT.format(
                query=query
            )

            # -------------------------------------------------------------
            # Automated Fallback Pool to handle 429 Resource Exhaustion
            # -------------------------------------------------------------
            model_pool = [
                "gemini-3.1-flash-lite",
                "gemini-2.5-flash",
                "gemini-2.0-flash"
            ]
            
            response = None
            for model_name in model_pool:
                try:
                    logger.info(f"Attempting query parsing with model: {model_name}")
                    response = self.client.models.generate_content(
                        model=model_name,
                        contents=prompt,
                        config={
                            "response_mime_type": "application/json"
                        }
                    )
                    # If successful, break out of the fallback loop immediately
                    break
                # except ClientError as e:
                #     # Check for 429 Rate Limit/Quota Exhaustion specifically
                #     if e.status_code == 429:
                #         logger.warning(f"⚠️ {model_name} rate limit reached. Attempting fallback model...")
                #         continue
                #     # If it's a different client error (e.g., 400 Bad Request), fail early
                #     raise e

                except Exception as e:

                    error_text = str(e)

                    if "429" in error_text:

                        logger.warning(
                            f"{model_name} rate limit reached. Trying fallback model..."
                        )

                        continue

                    logger.exception(
                        f"{model_name} failed"
                    )

                    raise
            # If the loop finished without getting a response from any model
            if response is None:
                raise RuntimeError(
                    "All available free tier Gemini models have exhausted their quotas. "
                    "Please wait 30–45 seconds before trying again."
                )

            # -------------------------------------------------------------
            # Parse and Normalize JSON Payload (Rest of your original logic)
            # -------------------------------------------------------------
            response_json = json.loads(
                response.text
            )

            # Normalize Empty Values
            for field in [
                "chapter",
                "section",
                "search_query"
            ]:
                if response_json.get(field) == "":
                    response_json[field] = None

            for field in [
                "page_start",
                "page_end"
            ]:
                if response_json.get(field) in ["", None]:
                    response_json[field] = None

            response_json.setdefault(
                "search_query",
                query
            )

            if not response_json.get(
                "search_query"
            ):
                response_json[
                    "search_query"
                ] = query

            # logger.info(
            #     f"Intent Parsed: {response_json}"
            # )

            # Normalize chapter
            if response_json.get("chapter") is not None:
                response_json["chapter"] = str(
                    response_json["chapter"]
                )

            # Normalize section
            if response_json.get("section") is not None:
                response_json["section"] = str(
                    response_json["section"]
                )

            # Normalize page numbers
            for field in [
                "page_start",
                "page_end"
            ]:
                value = response_json.get(field)

                if value in ["", None]:
                    response_json[field] = None
                else:
                    response_json[field] = int(value)

            # Normalize search_query
            if not response_json.get(
                "search_query"
            ):
                response_json[
                    "search_query"
                ] = query
            
            return QueryIntent(
                **response_json
            )