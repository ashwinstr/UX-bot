
from pyrogram import filters, Client

from jutsu import Config
from jutsu.plugins.warning import _admins_list_

owner = int(str(Config.OWNER_ID).split()[0])


@Client.on_message(
    filters.command(["testing"], prefixes="?")
    & filters.group
    & filters.user([764626151, 1503856346, 1156425647]),
    group=7
)
async def test(_, message):
    await message.reply("Working\n" + str([one for one in _admins_list_()]))
