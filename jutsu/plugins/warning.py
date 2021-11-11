# made by @Kakashi_HTK(TG)


import re
import time

from pyrogram import Client, filters
from pyrogram.types import ChatPermissions

from jutsu import get_collection

DATA = get_collection("USER_DATA")
ADMINS = get_collection("ADMINS")


@Client.on_message(
    filters.chat(["@Xplugin_support"])
    & filters.regex(r"^[(\.|\,|\!|\$|\^|\&|\(|\)|\~)][a-zA-Z]"),
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
    found = await DATA.find_one({'user': user_})
    if found:
        warnings = int(found['warnings'])
        warns = warnings + 1
        await DATA.update_one({'user': user_}, {"$set": {'warnings': warns}}, upsert=True)  
        if warns == 5:
            mute_for = 86400
            await bot.restrict_chat_member(
                message.chat.id, user_, ChatPermissions(), int(time.time() + mute_for) 
            )
            await DATA.update_one({'user': user_}, {"$set": {'warnings': 0}}, upsert=True)
            return await bot.send_message(message.chat.id, f"User **{user_men}** muted for **1 days** for 5th warn.")
    else:
        await DATA.insert_one({
            'user': user_,
            'warnings': 1
        })
        warns = 1
    info = f"""
**Warning** to **{user_men}**!!!
**Warn/s:** {warns}
```Bot won't work in this group. Go to Xplugin_OT.
You have been cautioned, 5th warn will be punishment.```
"""
    await bot.send_message(message.chat.id, info, reply_to_message_id=message.message_id)


@Client.on_message(
    filters.command(["resetwarns"], prefixes="?") & filters.user([1013414037]), group=3
)
async def reset_warns(bot, message):
    reply_ = message.reply_to_message
    if reply_:
        user_ = reply_.from_user.id
    else:
        try:
            user_ = (message.text).split(" ", 1)[1]
        except:
            return await bot.send_message(message.chat.id, "`Specify a user...`")
    try:
        user = await bot.get_users(user_)
    except:
        return await bot.send_message(message.chat.id, f"Provided user `{user_}` is not valid...")
    found = await DATA.find_one({'user': user.id})
    if found:
        await DATA.update_one({'user': user.id}, {"$set": {'warnings': 0}}, upsert=True)
        await bot.send_message(message.chat.id, f"The warnings for user **{user.mention}** has been reset.")
    else:
        await bot.send_message(message.chat.id, f"User **{user.mention}** has no warnings.")
