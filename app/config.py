from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    CLIENT_ID: str
    CLIENT_SECRET: str
    SCOPE: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
