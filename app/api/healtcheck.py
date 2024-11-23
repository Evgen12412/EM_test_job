from fastapi import APIRouter, status
from fastapi.openapi.models import Response

router = APIRouter()


@router.get("/healtcheck", include_in_schema=False)
async def get_healtcheck() -> Response:
    return Response(status_code=status.HTTP_200_OK)
