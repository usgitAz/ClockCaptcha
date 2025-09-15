import sys
import logging
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# basic loggign config if configs file faild !
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s - %(message)s"
)
logger = logging.getLogger("default")

# env file location
ENV_FILE_LOCATION = Path(__file__).resolve(
).parent.parent.parent.parent / ".env"

if not ENV_FILE_LOCATION.exists():
    logger.error("error env file not found ")
    raise FileNotFoundError("not .env file found in root directory !\n"
                            "Please create one by copying `.env.example` -> `.env`.")


class Settings(BaseSettings):
    # fastapi app
    app_name: str = "ClockCaptcha"
    app_version: str = Field(..., description="the version of this project")
    debug: bool = Field(
        default=False, description="debug mode, change to False for production!")

    # logging
    log_level_console: str = Field(
        default="DEBUG", description="log level for showing logs in console.")
    log_level_default: str = Field(
        default="DEBUG", description="log level for default logger")
    log_level_uvicorn: str = Field(
        default="DEBUG", description="log level for Uvicorn")

    model_config = SettingsConfigDict(
        env_file=str(ENV_FILE_LOCATION),
        env_file_encoding="utf-8",
    )


try:
    settings = Settings()
except Exception as error:
    logger.error(f"Error initializing project configs: {error}\n"
                 "Please make sure .env file exists and all required variables are set.")

    sys.exit(1)
