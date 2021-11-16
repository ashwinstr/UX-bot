
import os
import asyncio
import aiofiles

from pyrogram import Client, filters
from jutsu import Config, get_collection

ADMINS = get_collection("ADMINS")

owner = int(str(Config.OWNER_ID).split()[0])


""" async def _init():
    async for one in ADMINS.find():
        list_ = one['admin_ids']
        break
    async with aiofiles.open("cache/admin_list.txt", "w+") as fn:
        for one in list_:
            try:
                one = (await bot.get_users(one)).id
                await fn.writelines(f"{one}\n")      
            except:
                pass """


@Client.on_message(
    filters.command(["promote"], prefixes="?") & filters.user([owner]) & filters.group, group=2
)
async def add_admin(bot, message):
    msg = await bot.send_message(message.chat.id, "`Processing...`")
    reply_ = message.reply_to_message
    if not reply_:
        return await msg.edit("`Reply to a user to promote...`")
    user_ = await bot.get_users(reply_.from_user.id)
    chat_ = await bot.get_chat(message.chat.id)
    found = await ADMINS.find_one({"chat_id": chat_.id})
    admins = []
    if found:
        admins = found['admin_ids']
        if user_.id in admins:
            return await msg.edit(f"`User {user_.mention} is already admin for UX_JutsuBot in {chat_.title}...`")
    admins.append(user_.id)
    await ADMINS.update_one({'chat_id': chat_.id}, {'$set': {'admin_ids': admins}}, upsert=True)
    await msg.edit(f"`User {user_.mention} added in admin list of {chat_.title}.`")

    
@Client.on_message(
    filters.command(["demote"], prefixes="?") & filters.user([owner]) & filters.group, group=3
)
async def rem_admin(bot, message):
    msg = await bot.send_message(message.chat.id, "`Processing...`")
    reply_ = message.reply_to_message
    if not reply_:
        return await msg.edit("`Reply to a user to promote...`")
    user_ = await bot.get_users(reply_.from_user.id)
    chat_ = await bot.get_chat(message.chat.id)
    found = await ADMINS.find_one({"chat_id": chat_.id})
    if found:
        admins = found['admin_ids']
        if user_.id in admins:
            sr = 0
            for one in admins:
                if user_.id == found['admin_ids'][sr]:
                    break
                sr += 1
            admins.pop(sr)
            await ADMINS.update_one({'chat_id': chat_.id}, {'$set': {'admin_ids': admins}}, upsert=True)
            await msg.edit(f"`User {user_.mention} removed from admin for UX_JutsuBot in {chat_.title}...`")
            return
    await msg.edit("`User is not in admin list.`")

                                   
@Client.on_message(
    filters.command(["adlist"], prefixes="?") & filters.user([owner]) & filters.group, group=1
)
async def list_admins(bot, message):
    msg = await bot.send_message(message.chat.id, "`Checking admin list...`")
    found = await ADMINS.find_one({'chat_id': message.chat.id})
    if found:
        list_ = found['admin_ids']
        out_ = f"Admins of UX_JutsuBot in chat {message.chat.title}:\n\n"
        for mem in list_:
            user_ = await bot.get_users(int(mem))
            out_ += f"{user_.mention}\n"
        return await msg.edit(out_)
    else:
        await msg.edit("`There are no admins in this chat.`")


@Client.on_message(
    filters.command(["admincache"], prefixes="?")
    & filters.user([owner])
    & filters.group,
    group=4
)
async def admin_cache(bot, message):
    try:
        input_ = (message.text).split(" ", 1)[1]
    except:
        input_ = ""
    if "-c" in input_:
        with open("cache/admin_list.txt", "r") as reading:
            read_ = reading.read()
        read_ = read_.split()
        list_ = ""
        for one in read_:
            try:
                u_n = (await bot.get_users(int(one))).username
                u_n = f"- @{u_n}"
            except:
                u_n = ""
            list_ += f"`{one}` {u_n}\n"
        return await message.reply(list_)
    msg = await bot.send_message(message.chat.id, "`Refreshing admin list...`", reply_to_message_id=message.message_id)
    if not os.path.isdir("cache/"):
        os.mkdir("cache/")
    found = await ADMINS.find_one({'chat_id': -1001331162912})
    if not found:
        return await msg.edit("`List is empty.`")
    list_ = found['admin_ids']
    async with aiofiles.open("cache/admin_list.txt", "w+") as fn:
        for one in list_:
            try:
                one = (await bot.get_users(int(one))).id
                await fn.writelines(f"{one}\n")
            except:
                pass
    with open("cache/admin_list.txt", "r") as reading:
        read_ = reading.read()
    read_ = read_.split()
    list_ = ""
    for one in read_:
        try:
            u_n = (await bot.get_users(int(one))).username
            u_n = f"- @{u_n}"
        except:
            u_n = ""
        list_ += f"`{one}` {u_n}\n"
    await msg.edit(f"`Admin cache refreshed, users in the list are as below...`\n\n{list_}")
    asyncio.get_event_loop().create_task(bot.restart())
