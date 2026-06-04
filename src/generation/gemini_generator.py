from google import genai

from src.config.settings import settings
from src.prompts.rag_prompt import RAG_PROMPT
from src.utils.logger import (
    logger
)
import time
from src.utils.exceptions import (
    GenerationError
)

start_time = time.time()

class GeminiGenerator:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate(
        self,
        prompt: str
    ):

        logger.info(
            f"Generating Content | Prompt Length={len(prompt)}"
        )

        try:

            response = (
                self.client.models.generate_content(
                    model="gemini-2.5-flash-lite",
                    contents=prompt
                )
            )

            logger.info(
                f"Content Generated Successfully | "
                f"Duration={round(time.time()-start_time, 2)}s"
            )

            return response.text
        
        except Exception as e:

            logger.exception(
                "Gemini Generation Failed"
            )

            raise GenerationError(
                str(e)
            )

        # except Exception:

        #     logger.exception(
        #         "Gemini Generation Failed"
        #     )

        #     raise

    def generate_answer(
        self,
        question,
        context
    ):

        logger.info(
            f"Generating RAG Answer | Question={question}"
        )

        prompt = RAG_PROMPT.format(
            context=context,
            question=question
        )

        return self.generate(
            prompt
        )