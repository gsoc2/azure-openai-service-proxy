""" Request Manager base class """

from fastapi import APIRouter, Request, HTTPException

# pylint: disable=E0402
from ..authorize import Authorize, AuthorizeResponse
from ..config import Config
from ..deployment_class import DeploymentClass
from ..rate_limit import RateLimit


class RequestManager:
    """Request Manager base class"""

    def __init__(
        self,
        *,
        authorize: Authorize,
        config: Config,
        deployment_class: DeploymentClass,
        request_class_mgr,
    ):
        self.authorize = authorize
        self.deployment_class = deployment_class

        self.request_class_mgr = request_class_mgr(config, deployment_class)

        self.router = APIRouter()
        self.rate_limit = RateLimit()

    async def authorize_request(
        self, deployment_id: str, request: Request
    ) -> (AuthorizeResponse):
        """authorize request"""

        authorize_response = await self.authorize.authorize_api_access(
            headers=request.headers,
            deployment_id=deployment_id,
            request_class=self.deployment_class,
        )

        if self.rate_limit.is_call_rate_exceeded(authorize_response.user_token):
            raise HTTPException(
                status_code=429,
                detail="Rate limit exceeded. Try again in 10 seconds",
            )

        return authorize_response
