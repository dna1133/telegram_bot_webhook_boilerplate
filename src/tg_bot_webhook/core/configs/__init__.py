from src.tg_bot_webhook.core.configs.database import PostgresSettings
from src.tg_bot_webhook.core.configs.common import CommonSettings
from src.tg_bot_webhook.core.configs.logging import LoggingSettings
from src.tg_bot_webhook.core.configs.telegram import TelegramSettings


class Settings(
    PostgresSettings,
    TelegramSettings,
    LoggingSettings,
    CommonSettings,
):
    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
