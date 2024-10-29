from pydantic_settings import BaseSettings


class TelegramSettings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_BASE_WEBHOOK_URL: str
    TELEGRAM_WEBHOOK_PATH: str
    TELEGRAM_HOST: str
    TELEGRAM_PORT: int

    @property
    def TELEGRAM_WEB_HOOK(self) -> str:
        return f"{self.TELEGRAM_BASE_WEBHOOK_URL}{self.TELEGRAM_WEBHOOK_PATH}"
