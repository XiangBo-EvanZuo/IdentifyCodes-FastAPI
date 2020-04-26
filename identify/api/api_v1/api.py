from fastapi import APIRouter
from identify.core.config import settings
from identify.api.api_v1.endpoints import piccode

api_router = APIRouter()
api_router.include_router(piccode.router, prefix=settings.API_V1_STR, tags=["login"])