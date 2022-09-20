import asyncio


async def rocket_bot_tick():
    ...


async def rocket_bot_task():
    while 1:
        await rocket_bot_tick()
        await asyncio.sleep(1)
