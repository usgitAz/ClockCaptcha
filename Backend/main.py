from fastapi import FastAPI
from app.core.configs import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug

)
