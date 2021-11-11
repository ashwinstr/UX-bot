from pyrogram import filters, Client


SUGGESTION_LOG= "@Xplugin_suggestions"
BUG_LOG = "@Xplugin_Bugs"


@Client.on_message(
    filters.chat(["@xplugin_support"])
    & filters.regex(pattern=r"^#suggestion")
    & filters.group
    & ~filters.bot,
    group=1
)
async def sug_log(bot, message):
    text_ = message.text
    text_ = text_.replace("#suggestion", "")
    if not text_:
        await bot.send_message(message.chat.id, "`Suggestion message is empty, type suggestion tag and suggestion in same message.`")
        return
    mention = await bot.send_message(message.chat.id, f"Suggestion by **{message.from_user.mention}** logged successfully.")
    msg_ = await bot.copy_message(SUGGESTION_LOG, message.chat.id, message.message_id, reply_to_message_id=mention.message_id)
#    await bot.send_message(message.chat.id, "`Your suggestion has been logged, admins will look at it when they can...\nThank you.`", reply_to_message_id=message.message_id)
    if message.text:
        text_ = message.text
        text_ += f"{text_}\n\n### PENDING ###"
        await bot.edit_message_text(SUGGESTION_LOG, msg_.message_id, text_)
    elif message.caption:
        text_ = message.caption
        text_ += f"{text_}\n\n### PENDING ###"
        await bot.edit_message_caption(SUGGESTION_LOG, msg_.message_id, text_)

        
@Client.on_message(
    filters.chat(["@xplugin_support"])
    & filters.regex(pattern=r"^#bug")
    & filters.bot,
    group=2
)
async def bug_log(bot, message):
    text_ = message.text
    text_ = text_.replace("#bug", "")
    if not text_:
        await bot.send_message(message.chat.id, "`Bug report message is empty, type bug tag and bug report in same message.`")
        return
    mention = await bot.send_message(message.chat.id, f"Bug report by **{message.from_user.mention}** logged successfully.")
    msg_ = await bot.copy_message(BUG_LOG, message.chat.id, message.message_id, reply_to_message_id=mention.message_id)
#    await bot.send_message(message.chat.id, "`Your bug report has been logged, admins will look at it when they can...\nThank you.`", reply_to_message_id=message.message_id)
    if message.text:
        text_ = message.text
        text_ += f"{text_}\n\n### PENDING ###"
        await bot.edit_message_text(BUG_LOG, msg_.message_id, text_)
    elif message.caption:
        text_ = message.caption
        text_ += f"{text_}\n\n### PENDING ###"
        await bot.edit_message_caption(BUG_LOG, msg_.message_id, text_)
