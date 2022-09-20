import asyncio
import uvicorn

from src.configs import uvicorn_conf
from src.app import app

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    config = uvicorn.Config(**uvicorn_conf, loop=loop)
    server = uvicorn.Server(config)
    loop.create_task(server.serve())

    loop.run_forever()
