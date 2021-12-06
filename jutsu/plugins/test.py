
from pyrogram import filters, Client
from pyrogram.types import Message

from jutsu import Config
from .Admins import admins

owner = int(str(Config.OWNER_ID).split()[0])


admins_ = filters.create(admins)

@Client.on_message(
    filters.command(["testing"], prefixes="?")
    & filters.group
    & (admins_ | filters.user([owner])),
    group=7
)
async def test(bot, message: Message):
    await message.reply("Working\n" + message.input_str)
