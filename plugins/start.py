from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from database.blacklist import check_blacklist
from database.userchats import add_chat
from vars import var

START_MSG = """
Hi, I am **ANONYMOUS SENDER BOT.**\n
Just Forward me Some messages or
media and I will **Anonymize** that !!

You Can too Clone me :-
https://github.com/ProThinkerGang/Anonymous-Bot
"""


REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Caption Setting", callback_data="captz")],
        [InlineKeyboardButton("Support Group", url="t.me/FutureCodes")],
    ]
)


@Client.on_message(filters.command("start"))
async def start(client, message):
    fuser = message.from_user.id
    if check_blacklist(fuser):
        return
    add_chat(fuser)
    await message.reply_text(
        START_MSG, reply_markup=REPLY_MARKUP, disable_web_page_preview=True
    )
