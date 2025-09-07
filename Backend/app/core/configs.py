from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "ClockCaptcha"
    app_version: str = Field(
        "0.012", description="the version of this project")
    debug: bool = Field(
        default=False, description="debug mode, change to False for production!")

    # logging
    log_level_console: str = Field(
        default="DEBUG", description="log level for showing logs in console.")
    log_level_default: str = Field(
        default="DEBUG", description="log level for default logger")
    log_level_uvicorn: str = Field(
        default="DEBUG", description="log level for Uvicorn")


settings = Settings()
