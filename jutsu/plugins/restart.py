
import asyncio

from pyrogram import filters, Client
from jutsu import Config

owner = int(str(Config.OWNER_ID).split()[0]) 


@Client.on_message(
    filters.command(["restart"], prefixes="?")
    & filters.user([owner])
    & filters.group,
    group=5
)
async def restarting(bot, message):
    msg = await bot.send_message(message.chat.id, "`Restating app...`", reply_to_message_id=message.message_id)
    asyncio.get_event_loop().create_task(bot.restart())
    await msg.edit("`App restarted.`")
