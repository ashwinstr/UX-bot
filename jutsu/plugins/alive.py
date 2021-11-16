
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from jutsu.plugins.warning import owner


@Client.on_message(
    filters.command(["alive"], prefixes="?")
    & filters.group
    & filters.user([owner])
)
async def _alive(bot, message):
    alive_msg = f"""
**I'm alive.**
`See help for available commands.`
**Thank you.**
"""
    buttons_ = buttons()
    await bot.send_animation(
        message.chat.id,
        "resources/rinnegan-nagato.gif",
        caption=alive_msg,
        reply_to_message_id=message.message_id,
        reply_markup=buttons_,
    )

def buttons() -> InlineKeyboardMarkup:
    btn_ = [
        [
            InlineKeyboardButton(text="Support group", url="t.me/xplugin_support"),
            InlineKeyboardButton(text="OWNER", url="t.me/Kakashi_HTK"),
        ],
    ]
    return InlineKeyboardMarkup(btn_)
