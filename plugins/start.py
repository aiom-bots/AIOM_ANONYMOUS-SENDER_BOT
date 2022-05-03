from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from database.blacklist import check_blacklist
from database.userchats import add_chat
from vars import var

START_MSG = """
Hᴇʟʟᴏ 👋 {} ,

Tʜɪs Is Aɴᴏɴʏᴍᴏᴜs Sᴇɴᴅᴇʀ Bᴏᴛ

Yᴏᴜ Cᴀɴ Usᴇ Mᴇ Aɴᴏɴʏᴍɪᴢᴇ Tᴇʟᴇɢʀᴀᴍ Mᴇssᴀɢᴇs

Jᴜsᴛ Fᴏʀᴡᴀʀᴅ A Mᴇssᴀɢᴇ ᴏʀ Mᴇᴅɪᴀ Tᴏ Sᴛᴀʀᴛ

Pᴏᴡᴇʀᴅ Bʏ : @AIOM_BOTS
"""


REPLY_MARKUP = InlineKeyboardMarkup(
               [[
               InlineKeyboardButton("Caption Setting", callback_data="captz")
               ],[     
               InlineKeyboardButton("Support Group", url="t.me/FutureCodes")],
    ]
)


@Client.on_message(filters.command("start"))
async def start(client, message):
    fuser = message.from_user.id
    if check_blacklist(fuser):
        return
    add_chat(fuser)
    await message.reply(
        text=START_MSG.format(message.form_user.mention),
        reply_markup=REPLY_MARKUP,
        disable_web_page_preview=True
    )
