import asyncio
from datetime import datetime, timezone
import os
from rocketchat_API.rocketchat import RocketChat


def rocket_bot_logon() -> RocketChat:
    return RocketChat(
        user=os.getenv("BOT_USERNAME"),
        password=os.getenv("BOT_PASSWORD"),
        server_url=os.getenv("ROCKETCHAT_SERVER_URL"),
        ssl_verify=False,
    )


async def ping_command(rocket_client: RocketChat):
    """Response for ping command"""
    # TODO implement channel picking method
    channel = os.getenv("CHAT_NAME")
    messages = rocket_client.channels_history(
        channel,
        count=1,
    ).json()
    if messages["success"]:
        for message in messages["messages"]:
            if f'{os.getenv("BOT_PREFIX")}ping' in message["msg"]:
                time_now = datetime.now().astimezone()
                time_recv = datetime.strptime(
                    message["ts"], "%Y-%m-%dT%H:%M:%S.%fZ"
                ).astimezone()
                ping_time = (time_now - time_recv).total_seconds() / 1000
                rocket_client.chat_post_message(
                    f"{str(time_now).replace(':', '-')} ping: {ping_time:.3f} ms",
                    channel=channel,
                    alias="Bot",
                ).json()
    ...


async def rocket_bot_tick(rocket_client: RocketChat):
    await ping_command(rocket_client)
    ...


async def rocket_bot_task():
    rocket_client = rocket_bot_logon()
    while 1:
        await rocket_bot_tick(rocket_client)
        await asyncio.sleep(1)
