""" base class for model requests """

import logging
from typing import Tuple
from fastapi import HTTPException
import openai.openai_object

# pylint: disable=E0402
from .config import Config
from .management import DeploymentClass

# pylint: disable=E0402


class ModelRequest:
    """OpenAI Model Request"""

    def __init__(self, config: Config, deployment_class: DeploymentClass):
        """init in memory session manager"""
        self.config = config
        self.deployment_class = deployment_class
        self.logger = logging.getLogger(__name__)

    def throw_validation_error(self, message: str, status_code: int):
        """throw validation error"""
        raise HTTPException(
            status_code=status_code,
            detail=message,
        )

    def report_exception(
        self, message: str, http_status_code: int
    ) -> Tuple[openai.openai_object.OpenAIObject, int]:
        """report exception"""

        self.logger.warning(msg=f"{message}")

        raise HTTPException(
            status_code=http_status_code,
            detail=message,
        )
