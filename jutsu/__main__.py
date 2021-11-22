
import os
import pyrogram
from pyrogram import Client
from decouple import config



APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
STRING = config("STRING_SESSION", default=None)

async def genStrSession():  # pylint: disable=missing-function-docstring
    async with Client(
            "Jutsu",
            api_id=APP_ID,
            api_hash=API_HASH,
    ) as jutsu:
        string = await userge.export_session_string()
    return string

if __name__ == "__main__" :
    print("### Starting Bot... ###")
    plugins = dict(root="jutsu/plugins")
    app = pyrogram.Client(
        Client.export_session_string()
#        "sharingan",
#        STRING,
        bot_token=BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        
        plugins=plugins
    )
    app.run()
