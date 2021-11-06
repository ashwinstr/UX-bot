# ported from KensurBot and modified by @Kakashi_HTK(TG)


import re

from pyrogram import Client, filters

TRIGGERS = ('.', ',', '!', '$', '^', '&', '*', '(', ')', '~')

@Client.on_message(
    filters.regex(r"^[(\.|\,|\!|\$|\^|\&|\*|\(|\)|\~)]"),
    group=-1
)
async def block_(bot, message):
    chat_ = message.chat.id
    user_ = message.from_user.id
    status = await bot.get_chat_member(chat_, user_)
    is_admin = True if status.status== "administrator" else False
    is_creator = True if status.status == "creator" else False
    if is_admin or is_creator:
        return
    user_men = (await bot.get_users(user_)).mention
    info = f"""
**WARNING** to **{user_men}**!!!
```Bot won't work in this group.
You have been cautioned, next time will be a real warn.```
"""
    await bot.send_message(message.chat.id, info, reply_to_message_id=message.message_id)
