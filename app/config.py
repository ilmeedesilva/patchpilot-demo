from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "signup-service"
    debug: bool = False
    max_users: int = 100

    model_config = SettingsConfigDict(env_prefix="DEMO_")
