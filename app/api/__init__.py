from fastapi import APIRouter

from app.api import healtcheck, v1

router = APIRouter()

router.include_router(
    healtcheck.router,
    prefix='',
)

router.include_router(
    v1.router,
    prefix='/api/v1',
)
