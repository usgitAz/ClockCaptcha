from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "ClockCaptcha"
    app_version: str = Field(
        "0.012", description="the version of this project")
    debug: bool = Field(
        default=False, description="debug mode, change to False for production!")


settings = Settings()
