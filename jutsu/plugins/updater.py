import heroku3
import os
from os import system
import asyncio
import time

from pyrogram import Client, filters
from git import Repo
from git.exc import GitCommandError


HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_ENV = True
HEROKU_APP = (
        heroku3.from_key(HEROKU_API_KEY).apps()[HEROKU_APP_NAME]
        if HEROKU_ENV and HEROKU_API_KEY and HEROKU_APP_NAME
        else None
    )


@Client.on_message(
    filters.command(["update"], prefixes="?")
    & filters.user([1013414037]),
    group=0
)
async def updater_(bot, message):
    if HEROKU_APP:
        msg_ = await bot.send_message(
            message.chat.id,
            "`Restarting the bot...\nIt will take upto 10 sec to update.`",
        )
        HEROKU_APP.restart()
        time.sleep(10)
    else:
        await bot.send_message(message.chat.id, "`Restarting [HARD] ...`")
        asyncio.get_event_loop().create_task(bot.restart(hard=True))
