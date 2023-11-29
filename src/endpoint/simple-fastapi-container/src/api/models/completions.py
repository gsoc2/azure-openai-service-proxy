""" Completions API """

import logging
from typing import Tuple, Any

from pydantic import BaseModel
import openai
import openai.error
import openai.openai_object

# pylint: disable=E0402
from ..authorize import AuthorizeResponse
from ..openai_async import OpenAIAsyncManager
from .request_base import ModelRequest

OPENAI_COMPLETIONS_API_VERSION = "2023-09-01-preview"

logging.basicConfig(level=logging.WARNING)


class CompletionsRequest(BaseModel):
    """OpenAI Compeletion Request"""

    prompt: str | list[str]
    max_tokens: int = None
    temperature: float = None
    top_p: float | None = None
    stop: Any | None = None
    frequency_penalty: float = 0
    presence_penalty: float = 0
    api_version: str = OPENAI_COMPLETIONS_API_VERSION


class Completions(ModelRequest):
    """OpenAI Completions Manager"""

    def __validate_input(self, cr: CompletionsRequest):
        """validate input"""
        # do some basic input validation
        if not cr.prompt:
            return self.report_exception("Oops, no prompt.", 400)

        # check the max_tokens is between 1 and 4000
        if cr.max_tokens and not 1 <= cr.max_tokens <= 4000:
            return self.report_exception(
                "Oops, max_tokens must be between 1 and 4000.", 400
            )

        # check the temperature is between 0 and 1
        if cr.temperature and not 0 <= cr.temperature <= 1:
            return self.report_exception(
                "Oops, temperature must be between 0 and 1.", 400
            )

        # check the top_p is between 0 and 1
        if cr.top_p and not 0 <= cr.top_p <= 1:
            return self.report_exception("Oops, top_p must be between 0 and 1.", 400)

        # check the frequency_penalty is between 0 and 1
        if cr.frequency_penalty and not 0 <= cr.frequency_penalty <= 1:
            return self.report_exception(
                "Oops, frequency_penalty must be between 0 and 1.", 400
            )

        # check the presence_penalty is between 0 and 1
        if cr.presence_penalty and not 0 <= cr.presence_penalty <= 1:
            return self.report_exception(
                "Oops, presence_penalty must be between 0 and 1.", 400
            )

        # check stop sequence are printable characters
        if cr.stop and not cr.stop.isprintable():
            return self.report_exception(
                "Oops, stop_sequence must be printable characters.", 400
            )

    async def call_openai_completion(
        self,
        cr: CompletionsRequest,
        authorize_response: AuthorizeResponse,
    ) -> Tuple[openai.openai_object.OpenAIObject, int]:
        """call openai with retry"""

        self.__validate_input(cr)

        deployment = await self.config.get_deployment(authorize_response)

        openai_request = {
            "prompt": cr.prompt,
            "max_tokens": cr.max_tokens,
            "temperature": cr.temperature,
            "top_p": cr.top_p,
            "stop": cr.stop,
            "frequency_penalty": cr.frequency_penalty,
            "presence_penalty": cr.presence_penalty,
        }

        url = (
            f"https://{deployment.resource_name}.openai.azure.com/openai/deployments/"
            f"{deployment.deployment_name}/completions"
            f"?api-version={cr.api_version}"
        )

        async_mgr = OpenAIAsyncManager(deployment)
        response = await async_mgr.async_openai_post(openai_request, url)

        response["model"] = deployment.friendly_name

        return response, 200
