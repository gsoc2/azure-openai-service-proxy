""" dalle-3 and beyond """

from fastapi import Request, Response, FastAPI

# pylint: disable=E0402
from ..authorize import Authorize
from ..config import Config
from ..deployment_class import DeploymentClass
from ..images import ImagesRequest, Images as RequestMgr
from .request_manager import RequestManager


class Images(RequestManager):
    """Completion route"""

    def __init__(
        self,
        app: FastAPI,
        authorize: Authorize,
        config: Config,
        prefix: str,
        tags: list[str],
    ):
        super().__init__(
            app=app,
            authorize=authorize,
            config=config,
            prefix=prefix,
            tags=tags,
            deployment_class=DeploymentClass.OPENAI_IMAGES.value,
            request_class_mgr=RequestMgr,
        )

        self.__include_router()

    def __include_router(self):
        """include router"""

        # Support for Dall-e-3 and beyond
        # Azure OpenAI Images
        @self.router.post(
            "/openai/deployments/{deployment_id}/images/generations",
            status_code=200,
            response_model=None,
        )
        # OpenAI Images
        @self.router.post(
            "/images/generations",
            status_code=200,
            response_model=None,
        )
        async def oai_images(
            images_request: ImagesRequest,
            request: Request,
            response: Response,
            deployment_id: str = None,
        ):
            """OpenAI image generation response"""

            # get the api version from the query string
            if "api-version" in request.query_params:
                images_request.api_version = request.query_params["api-version"]

            # exception thrown if not authorized
            authorize_response = await self.authorize_request(
                deployment_id=deployment_id, request=request
            )

            (
                completion_response,
                status_code,
            ) = await self.request_class_mgr.call_openai_images_generations(
                images_request, authorize_response
            )
            response.status_code = status_code
            return completion_response

        self.app.include_router(self.router, prefix=self.prefix, tags=self.tags)
