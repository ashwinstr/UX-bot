from pyrogram import filters, Client


LOG_CHANNEL = "@Xplugin_suggestions"


@Client.on_message(
    filters.chat([-1001331162912])
    & filters.regex(pattern=r"^#suggestion"),
    group=1
)
async def sug_log(bot, message):
    mention = await bot.send_message(message.chat.id, f"Suggestion by **{message.from_user.mention}** logged successfully.")
    msg_ = await bot.copy_message(LOG_CHANNEL, message.chat.id, message.message_id, reply_to_message_id=mention.message_id)
    await bot.send_message(message.chat.id, "`Your suggestion has been logged, admins will look at it when they can...\nThank you.`", reply_to_message_id=message.message_id)
    if message.text:
        text_ = message.text
        text_ += f"{text_}\n\n### PENDING ###"
        await bot.edit_message_text(LOG_CHANNEL, msg_.message_id, text_)
    elif message.caption:
        text_ = message.caption
        text_ += f"{text_}\n\n### PENDING ###"
        await bot.edit_message_caption(LOG_CHANNEL, msg_.message_id, text_)

        
@Client.on_message(
    filters.chat([-1001331162912])
    & filters.regex(pattern=r"^#bug"),
    group=1
)
async def sug_log(bot, message):
    mention = await bot.send_message(message.chat.id, f"Bug report by **{message.from_user.mention}** logged successfully.")
    msg_ = await bot.copy_message(LOG_CHANNEL, message.chat.id, message.message_id, reply_to_message_id=mention.message_id)
    await bot.send_message(message.chat.id, "`Your bug report has been logged, admins will look at it when they can...\nThank you.`", reply_to_message_id=message.message_id)
    if message.text:
        text_ = message.text
        text_ += f"{text_}\n\n### PENDING ###"
        await bot.edit_message_text(LOG_CHANNEL, msg_.message_id, text_)
    elif message.caption:
        text_ = message.caption
        text_ += f"{text_}\n\n### PENDING ###"
        await bot.edit_message_caption(LOG_CHANNEL, msg_.message_id, text_)
