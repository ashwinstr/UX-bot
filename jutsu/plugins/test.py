
from pyrogram import filters, Client

from jutsu import Config, app
from jutsu.helpers import _admins_list_
from jutsu.plugins.Admins import admins

owner = int(str(Config.OWNER_ID).split()[0])


admins_ = filters.create(admins)

@Client.on_message(
    filters.command(["testing"], prefixes="?")
    & filters.group
    & (admins_ | filters.user([owner])),
    group=7
)
async def test(bot, message):
    await message.reply("Working\n" + str(admins_))
