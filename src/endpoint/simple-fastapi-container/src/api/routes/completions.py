""" completion routes """

from typing import Any, Tuple
from pydantic import BaseModel
from fastapi import Request, Response
import openai.openai_object

# pylint: disable=E0402
from ..authorize import Authorize
from ..config import Config, Deployment
from ..deployment_class import DeploymentClass
from ..openai_async import OpenAIAsyncManager
from .request_manager import RequestManager

OPENAI_COMPLETIONS_API_VERSION = "2023-09-01-preview"


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


class Completions(RequestManager):
    """Completion route"""

    def __init__(
        self,
        authorize: Authorize,
        config: Config,
    ):
        super().__init__(
            authorize=authorize,
            config=config,
            deployment_class=DeploymentClass.OPENAI_COMPLETIONS.value,
            # request_class_mgr=None,
        )

    def include_router(self):
        """include router"""

        # Support for OpenAI SDK 0.28
        @self.router.post(
            "/engines/{engine_id}/completions",
            status_code=200,
            response_model=None,
        )
        # Support for Azure OpenAI Service SDK 1.0+
        @self.router.post(
            "/openai/deployments/{deployment_id}/completions",
            status_code=200,
            response_model=None,
        )
        # Support for OpenAI SDK 1.0+
        @self.router.post("/completions", status_code=200, response_model=None)
        async def oai_completion(
            model: CompletionsRequest,
            request: Request,
            response: Response,
            deployment_id: str = None,
        ) -> openai.openai_object.OpenAIObject | str:
            """OpenAI completion response"""

            completion, status_code = await self.process_request(
                deployment_id=deployment_id,
                request=request,
                model=model,
                call_method=self.call_openai,
                validate_method=self.__validate_completion_request,
            )

            response.status_code = status_code
            return completion

        return self.router

    async def call_openai(
        self,
        model: CompletionsRequest,
        openai_request: dict[str, Any],
        deployment: Deployment,
    ) -> Tuple[openai.openai_object.OpenAIObject, int]:
        """call openai with retry"""

        url = (
            f"https://{deployment.resource_name}.openai.azure.com/openai/deployments/"
            f"{deployment.deployment_name}/completions"
            f"?api-version={model.api_version}"
        )

        async_mgr = OpenAIAsyncManager(deployment)
        response = await async_mgr.async_openai_post(openai_request, url)

        response["model"] = deployment.friendly_name

        return response, 200

    def __validate_completion_request(self, model: CompletionsRequest):
        if not model.prompt:
            self.report_exception("Oops, no prompt.", 400)
