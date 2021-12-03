
import pyrogram
from pyrogram import Client, filters
from decouple import config



APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
STRING = config("STRING_SESSION", default=None)


jutsu = Client(":memory:", api_hash=API_HASH, api_id=APP_ID, bot_token=BOT_TOKEN)

@jutsu.on_message(
    filters.me & filters.command("start", prefixes="?")
)
async def session(jutsu, message):
    await message.reply(f"The session string is as below...\n\n`{str(jutsu.export_session_string())}`\n\nUse it wisely.")


session_string = ""

if __name__ == "__main__" :
    print("### Starting Bot... ###")
    plugins = dict(root="jutsu/plugins")
    if session_string:
        string = session_string
    else:
        string = ":memory:"
    app = pyrogram.Client(
        string,
        bot_token=BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        
        plugins=plugins
    )
    app.run()
