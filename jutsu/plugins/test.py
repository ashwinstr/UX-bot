
from pyrogram import filters, Client

from jutsu import Config, app
from jutsu.plugins.warning import _admins_list_
from .admins import Admins

owner = int(str(Config.OWNER_ID).split()[0])


admins_ = filters.create(_, __, ___: Admins)

@app.on_message(
    filters.command(["testing"], prefixes="?")
    & filters.group
    & admins_,
    group=7
)
async def test(bot, message):
    await message.reply("Working\n" + str([one for one in _admins_list_()]))
