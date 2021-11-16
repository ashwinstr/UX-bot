
from pyrogram import filters, Client

from jutsu import Config
from jutsu.plugins.warning import _admins_list_

owner = int(str(Config.OWNER_ID).split()[0])


@Client.on_message(
    filters.command(["testing"], prefixes="?")
    & filters.group,
    group=7
)
async def test(bot, message):
    if message.from_user.id not in _admins_list_():
        return
    await message.reply("Working\n" + str([one for one in _admins_list_()]))
    await bot.send_message(message.chat.id, "test")
