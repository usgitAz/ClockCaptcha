from fastapi import FastAPI
from app.core.configs import settings

# initial logging config at First
from app.core.logging_config import setup_logging
setup_logging()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug

)