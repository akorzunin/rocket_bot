import asyncio
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src import shemas

router = APIRouter()


@router.get(
    "/test",
    response_model=shemas.Message,
    status_code=status.HTTP_202_ACCEPTED,
)
async def test_endpoint(
    message: str,
):
    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED,
        content=shemas.Message(message=message).dict(),
    )
