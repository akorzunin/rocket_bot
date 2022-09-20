import asyncio
import logging
from fastapi import FastAPI

from src.api_routes import router as api_routes
from src.front_routes import router as front_routes
from src.metadata import tags_metadata
from src.logger import format as log_format
from src.rocket_bot_handler import rocket_bot_task


app = FastAPI(
    openapi_tags=tags_metadata,
)


@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger("uvicorn.access")
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(log_format))
    # add logs to stdout
    logger.removeHandler(logger.handlers[0])
    logger.addHandler(handler)
    # add task handler to event loop
    loop = asyncio.get_event_loop()
    loop.create_task(
        coro=rocket_bot_task(),
        name="rocket_bot_task",
    )


app.include_router(
    router=front_routes,
    tags=["Frontend"],
)
app.include_router(
    router=api_routes,
    prefix="/api",
    tags=["API"],
)
