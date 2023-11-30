""" dalle-2 """

from os import environ
from enum import Enum
from typing import Tuple
from fastapi import Request, Response
from pydantic import BaseModel
import openai.openai_object

# pylint: disable=E0402
from ..authorize import Authorize
from ..config import Config, Deployment
from ..deployment_class import DeploymentClass
from .request_manager import RequestManager
from ..authorize import AuthorizeResponse
from ..openai_async import OpenAIAsyncManager

OPENAI_IMAGES_GENERATIONS_API_VERSION = "2023-06-01-preview"


class ResponseFormat(Enum):
    """Response Format"""

    URL = "url"
    BASE64 = "b64_json"


class ImageSize(Enum):
    """Image Size"""

    IS_256X256 = "256x256"
    IS_512X512 = "512x512"
    IS_1024X1024 = "1024x1024"


class DalleTimeoutError(Exception):
    """Raised when the Dalle request times out"""


class ImagesGenerationsRequst(BaseModel):
    """OpenAI Images Generations Request"""

    prompt: str
    response_format: ResponseFormat = ResponseFormat.URL
    n: int = 1
    size: ImageSize = ImageSize.IS_1024X1024
    user: str = None
    api_version: str = OPENAI_IMAGES_GENERATIONS_API_VERSION


class ImagesGenerations(RequestManager):
    """Completion route"""

    def __init__(
        self,
        authorize: Authorize,
        config: Config,
    ):
        super().__init__(
            authorize=authorize,
            config=config,
            deployment_class=DeploymentClass.OPENAI_IMAGES_GENERATIONS.value,
        )

    def include_router(self):
        """include router"""

        # Support for Dall-e-2
        # Support for OpenAI SDK 0.28
        @self.router.post(
            "/engines/{engine_id}/images/generations",
            status_code=200,
            response_model=None,
        )
        # Support for Azure OpenAI Service SDK 1.0+
        @self.router.post(
            "/openai/images/generations:submit",
            status_code=200,
            response_model=None,
        )
        async def oai_images_generations(
            model: ImagesGenerationsRequst,
            request: Request,
            response: Response,
        ):
            """OpenAI image generation response"""

            # No deployment_is passed for images generation so set to dall-e
            deployment_id = "dall-e"

            authorize_response = await self.authorize.authorize_api_access(
                headers=request.headers,
                deployment_id=deployment_id,
                request_class=self.deployment_class,
            )

            completion, status_code = await self.call_openai_images_generations(
                model, request, response, authorize_response
            )

            response.status_code = status_code

            return completion

        @self.router.get("/{friendly_name}/openai/operations/images/{image_id}")
        async def oai_images_get(
            friendly_name: str,
            image_id: str,
            request: Request,
            response: Response,
        ):
            """OpenAI image generation response"""

            # No deployment_is passed for images generation so set to dall-e
            deployment_id = "dall-e"

            if "api-version" in request.query_params:
                api_version = request.query_params["api-version"]

            authorize_response = await self.authorize_request(
                deployment_id=deployment_id, request=request
            )

            (completion_response, status_code,) = await self.call_openai_images_get(
                friendly_name,
                image_id,
                authorize_response,
                api_version,
            )

            response.status_code = status_code
            return completion_response

        return self.router

    async def call_openai_images_generations(
        self,
        images: ImagesGenerationsRequst,
        request: Request,
        response: Response,
        authorize_response: AuthorizeResponse,
    ) -> Tuple[Deployment, openai.openai_object.OpenAIObject, int]:
        """call openai with retry"""

        self.validate_input(images)

        deployment = await self.config.get_deployment(authorize_response)

        openai_request = {
            "prompt": images.prompt,
            "n": images.n,
            "size": images.size.value,
            "response_format": images.response_format.value,
        }

        url = (
            f"https://{deployment.resource_name}.openai.azure.com"
            "/openai/images/generations:submit"
            f"?api-version={images.api_version}"
        )

        async_mgr = OpenAIAsyncManager(deployment)
        dalle_response = await async_mgr.async_post(openai_request, url)

        if "operation-location" in dalle_response.headers:
            original_location = dalle_response.headers["operation-location"]
            port = f":{request.url.port}" if request.url.port else ""
            original_location_suffix = original_location.split("/openai", 1)[1]

            if environ.get("ENVIRONMENT") == "development":
                proxy_location = (
                    f"http://{request.url.hostname}{port}"
                    f"/v1/api/{deployment.friendly_name}/openai{original_location_suffix}"
                )
            else:
                proxy_location = (
                    f"https://{request.url.hostname}{port}"
                    f"/v1/api/{deployment.friendly_name}/openai{original_location_suffix}"
                )

            response.headers.append("operation-location", proxy_location)

        return dalle_response.json(), dalle_response.status_code

    async def call_openai_images_get(
        self,
        friendly_name: str,
        image_id: str,
        authorize_response: AuthorizeResponse,
        api_version: str = OPENAI_IMAGES_GENERATIONS_API_VERSION,
    ):
        """call openai with retry"""

        deployment = await self.config.get_deployment_by_name(
            friendly_name, authorize_response
        )

        if deployment is None:
            return self.report_exception(
                "Oops, failed to find service to generate image.", 404
            )

        url = (
            f"https://{deployment.resource_name}.openai.azure.com"
            f"/openai/operations/images/{image_id}"
            f"?api-version={api_version}"
        )

        async_mgr = OpenAIAsyncManager(deployment)
        dalle_response = await async_mgr.async_get(url)

        return dalle_response.json(), dalle_response.status_code

    def validate_input(self, images: ImagesGenerationsRequst):
        """validate input"""
        # do some basic input validation
        if not images.prompt:
            self.report_exception("Oops, no prompt.", 400)

        if len(images.prompt) > 1000:
            self.report_exception(
                "Oops, prompt is too long. The maximum length is 1000 characters.", 400
            )

        # check the image_count is between 1 and 5
        if images.n and not 1 <= images.n <= 5:
            self.report_exception(
                "Oops, image_count must be between 1 and 5 inclusive.", 400
            )

        # check the image_size is between 256x256, 512x512, 1024x1024
        if images.size and images.size not in ImageSize:
            self.report_exception(
                "Oops, image_size must be 256x256, 512x512, 1024x1024.", 400
            )

        # check the response_format is url or base64
        if images.response_format and images.response_format not in ResponseFormat:
            self.report_exception("Oops, response_format must be url or b64_json.", 400)
