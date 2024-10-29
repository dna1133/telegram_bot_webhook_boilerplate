from enum import StrEnum, auto
from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggingSettings(BaseSettings):
    LOGGING_LEVEL: str
