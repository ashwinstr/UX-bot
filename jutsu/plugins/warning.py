# made by @Kakashi_HTK(TG)


import re
import time
import os

from pyrogram import Client, filters
from pyrogram.types import ChatPermissions, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from jutsu import get_collection, Config
from .Admins import admins


DATA = get_collection("USER_DATA")
ADMINS = get_collection("ADMINS")

owner = int(str(Config.OWNER_ID).split()[0])


admins = filters.create(admins)

@Client.on_message(
    filters.chat(["@UX_xplugin_support"])
    & filters.regex(r"^[(\.|\,|\$|\^|\&|\(|\)|\~)][a-zA-Z]")
    & filters.group,
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
            return await bot.send_message(message.chat.id, f"User **{user_men}** muted for **1 day** for 5th warn.")
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
    await bot.send_message(message.chat.id, info, reply_to_message_id=message.message_id, reply_markup=buttons())


@Client.on_callback_query(
    filters.regex(r"remove_.*")
)
async def remove_warn(bot, c_q: CallbackQuery):
    try:
        found = await ADMINS.find_one({"chat_id": c_q.message.chat.id})
        if not found:
            return
        if c_q.from_user.id not in found['admin_ids'] and c_q.from_user.id != Config.OWNER_ID:
            await c_q.answer("Only admins approved by Kakashi can do this.", show_alert=True)
            return
        reply_ = c_q.message.reply_to_message
        user_ = reply_.from_user.id
        if "one" in str(c_q.data):
            user_d = await DATA.find_one({"user": user_})
            warns = int(user_d['warnings']) - 1
            await DATA.update_one({'user': user_}, {"$set": {'warnings': warns}}, upsert=True)
            await c_q.edit_message_text(f"One warning removed, user {reply_.from_user.mention} currently has {warns} warns.")
        elif "all" in str(c_q.data):
            await DATA.update_one({'user': user_}, {"$set": {'warnings': 0}}, upsert=True)
            await c_q.edit_message_text(f"Warnings reset for {reply_.from_user.mention}.")
    except Exception as e:
        await bot.send_message(Config.LOG_CHANNEL, e)


@Client.on_message(
    filters.command(["resetwarns"], prefixes="?") & (admins | filters.user([owner])), group=-2
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


def buttons() -> InlineKeyboardMarkup:
    btn_ = [
        [
            InlineKeyboardButton(text="Remove one warn.", callback_data="remove_one"),
        ],
        [
            InlineKeyboardButton(text="Reset all warns.", callback_data="remove_all"),
        ],
    ]
    return InlineKeyboardMarkup(btn_)