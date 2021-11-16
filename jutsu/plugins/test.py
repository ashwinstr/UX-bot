
from pyrogram import filters, Client

from jutsu import Config
from jutsu.plugins.warning import _admins_list_

owner = int(str(Config.OWNER_ID).split()[0])


@Client.on_message(
    filters.command(["testing"], prefixes="?")
    & filters.group
    & filters.user([one for one in _admins_list_()]),
    group=7
)
async def test(bot, message):
    await message.reply("Working\n" + [one for one in _admins_list()])
