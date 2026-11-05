from functools import lru_cache
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="SYJ_", extra="ignore")
    environment: str = "development"
    database_url: str = "postgresql+asyncpg://syj:syj_dev_only@postgres:5432/syj_voice"
    jwt_secret: SecretStr = SecretStr("CHANGE_ME_BEFORE_USE_32_CHAR_MINIMUM")
    jwt_issuer: str = "syj-voice"
    access_token_minutes: int = 10
    refresh_token_days: int = 14
    cors_origins: str = "http://localhost:3000"
    redis_url: str = "redis://redis:6379/0"
    @property
    def allowed_origins(self) -> list[str]:
        return [x.strip() for x in self.cors_origins.split(",") if x.strip()]

@lru_cache
def get_settings() -> Settings:
    return Settings()
