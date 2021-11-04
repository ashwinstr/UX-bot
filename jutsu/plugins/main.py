# ported from KensurBot and modified by @Kakashi_HTK(TG)


import re
from sre_constants import error as sre_err

from pyrogram import Client, filters
from pyrogram.errors import MessageDeleteForbidden

TRIGGERS = ('.', ',', '!', '$', '^', '&', '*', '(', ')', '~')

@Client.on_message(
    filters.regex(r"^\{}".format(trig for trig in TRIGGERS)),
    group=-1
)
async def block_(bot, message):
    info = f"""
**WARNING:**
Bot won't work in this group.
You have been warned, next time will be a warn.
"""
    await bot.send_message(message.chat.id, info)
