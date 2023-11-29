""" Chat Completions API """

import logging
from typing import Tuple, Any, AsyncGenerator

from pydantic import BaseModel
import openai
import openai.error
import openai.openai_object

# pylint: disable=E0402
from .authorize import AuthorizeResponse
from .openai_async import OpenAIAsyncManager
from .request_base import ModelRequest

OPENAI_CHAT_COMPLETIONS_API_VERSION = "2023-09-01-preview"
OPENAI_CHAT_COMPLETIONS_EXTENSIONS_API_VERSION = "2023-08-01-preview"

logging.basicConfig(level=logging.WARNING)


class ChatCompletionsRequest(BaseModel):
    """OpenAI Chat Request"""

    messages: list[dict[str, str]]
    dataSources: list[Any] | None = None
    max_tokens: int = None
    temperature: float = None
    n: int | None = None
    stream: bool = False
    top_p: float | None = None
    stop: str | list[str] | None = None
    frequency_penalty: float | None = None
    presence_penalty: float | None = None
    functions: list[dict[str, Any]] | None = None
    function_call: str | dict[str, str] | None = None
    api_version: str | None = None
    extensions: bool = False


class ChatCompletions(ModelRequest):
    """OpenAI Chat Completions Manager"""

    def validate_input(self, chat: ChatCompletionsRequest):
        """validate input"""
        # do some basic input validation

        # check the max_tokens is between 1 and 4096
        if chat.max_tokens is not None and not 1 <= chat.max_tokens <= 4096:
            self.throw_validation_error(
                "Oops, max_tokens must be between 1 and 4096.", 400
            )

        if chat.n is not None and not 1 <= chat.n <= 10:
            self.throw_validation_error("Oops, n must be between 1 and 10.", 400)

        # check the temperature is between 0 and 1
        if chat.temperature is not None and not 0 <= chat.temperature <= 1:
            self.throw_validation_error(
                "Oops, temperature must be between 0 and 1.", 400
            )

        # check the top_p is between 0 and 1
        if chat.top_p is not None and not 0 <= chat.top_p <= 1:
            self.throw_validation_error("Oops, top_p must be between 0 and 1.", 400)

        # check the frequency_penalty is between 0 and 1
        if chat.frequency_penalty is not None and not 0 <= chat.frequency_penalty <= 1:
            self.throw_validation_error(
                "Oops, frequency_penalty must be between 0 and 1.", 400
            )

        # check the presence_penalty is between 0 and 1
        if chat.presence_penalty is not None and not 0 <= chat.presence_penalty <= 1:
            self.throw_validation_error(
                "Oops, presence_penalty must be between 0 and 1.", 400
            )

    async def call_openai_chat_completion(
        self,
        chat: ChatCompletionsRequest,
        authorize_response: AuthorizeResponse,
    ) -> Tuple[openai.openai_object.OpenAIObject, int] | AsyncGenerator:
        """call openai with retry"""

        self.validate_input(chat)
        deployment = await self.config.get_deployment(authorize_response)

        # if dataSources are provided, use the extensions API
        if chat.extensions:
            api_version = (
                chat.api_version or OPENAI_CHAT_COMPLETIONS_EXTENSIONS_API_VERSION
            )
            url = (
                f"https://{deployment.resource_name}.openai.azure.com/openai/deployments/"
                f"{deployment.deployment_name}/extensions/chat/completions"
                f"?api-version={api_version}"
            )
        else:
            api_version = chat.api_version or OPENAI_CHAT_COMPLETIONS_API_VERSION
            url = (
                f"https://{deployment.resource_name}.openai.azure.com/openai/deployments/"
                f"{deployment.deployment_name}/chat/completions"
                f"?api-version={api_version}"
            )

        del chat.extensions
        del chat.api_version

        openai_request = {}

        for key, value in chat.__dict__.items():
            if value is not None:
                openai_request[key] = value

        async_mgr = OpenAIAsyncManager(deployment)

        if chat.stream:
            response = await async_mgr.async_post_streaming(openai_request, url)
        else:
            response = await async_mgr.async_openai_post(openai_request, url)
            response["model"] = deployment.friendly_name

        return response, 200
