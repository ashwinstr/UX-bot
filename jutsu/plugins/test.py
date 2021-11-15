
from pyrogram import filters, Client

from jutsu import Config
from jutsu.plugins.warning import _admins_list_

owner = int(str(Config.OWNER_ID).split()[0])


@Client.on_message(
    filters.command(["testing"], prefixes="?")
    & filters.group
    & filters.user([1156425647]),
    group=7
)
async def test(bot, message):
    await bot.send_message(message.chat.id, "Working", reply_to_message_id=message.message_id)
