import logging.config
from pathlib import Path
from app.core.configs import settings

LOGS_BASE_DIR = Path(__file__).parent.parent.parent / "logs"
LOGS_BASE_DIR.mkdir(parents=True, exist_ok=True)

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "detailed": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
        "simple": {
            "format": "%(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": settings.log_level_console,
            "formatter": "detailed"
        },
        "default": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "detailed",
            "filename": str(LOGS_BASE_DIR / "default" / "default.log"),
            "maxBytes": 10 * 1024 * 1024,  # 10mb
            "backupCount": 2
        },
        "uvicorn_error_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "WARNING",
            "formatter": "detailed",
            "filename": str(LOGS_BASE_DIR / "uvicorn" / "uvicorn_error.log"),
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 2
        },
        "uvicorn_access_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "detailed",
            "filename": str(LOGS_BASE_DIR / "uvicorn" / "uvicorn_access.log"),
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 2
        }

    },
    "loggers": {
        "default": {
            "level": settings.log_level_default,
            "handlers": ["console", "default"],
            "propagate": False
        },
        "uvicorn.error": {
            "level": settings.log_level_uvicorn,
            "handlers": ["console", "uvicorn_error_file"],
            "propagate": False
        },
        "uvicorn.access": {
            "level": settings.log_level_uvicorn,
            "handlers": ["console", "uvicorn_access_file"],
            "propagate": False
        }
    }
}


def setup_logging():
    """
    initial custom logging config with dictionary format 
    """

    (LOGS_BASE_DIR / "default").mkdir(parents=True, exist_ok=True)
    (LOGS_BASE_DIR / "uvicorn").mkdir(parents=True, exist_ok=True)

    logging.config.dictConfig(LOGGING_CONFIG)
