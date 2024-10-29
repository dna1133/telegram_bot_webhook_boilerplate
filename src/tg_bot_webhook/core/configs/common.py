from enum import Enum

from pydantic_settings import BaseSettings


class Environment(str, Enum):
    DEV = "dev"
    PROD = "prod"
    TEST = "test"


class CommonSettings(BaseSettings):
    SERVICE_NAME: str = "telegram_bot_webhook_boilerplate"
    ENVIRONMENT: Environment = Environment.DEV
