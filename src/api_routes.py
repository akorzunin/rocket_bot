import asyncio
import os
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src import shemas
from src.rocket_bot_handler import rocket_bot_logon

router = APIRouter()


@router.on_event("startup")
async def startup_event():
    # TODO use different implementation for logon object
    global rocket_client
    rocket_client = rocket_bot_logon()


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


@router.post(
    "/notify_arrived",
    status_code=status.HTTP_202_ACCEPTED,
)
async def notify_arrived():
    message = rocket_client.chat_post_message(
        "Notification message",
        channel=os.getenv("CHAT_NAME"),
        alias="🚗🍕🍔",
    )
    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED, content=message.json()
    )
