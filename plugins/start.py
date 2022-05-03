from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from database.blacklist import check_blacklist
from database.userchats import add_chat
from vars import var

START_MSG = """
<b>Hᴇʟʟᴏ 👋 {} ,

Tʜɪs Is Aɴᴏɴʏᴍᴏᴜs Sᴇɴᴅᴇʀ Bᴏᴛ

Yᴏᴜ Cᴀɴ Usᴇ Mᴇ Aɴᴏɴʏᴍɪᴢᴇ Tᴇʟᴇɢʀᴀᴍ Mᴇssᴀɢᴇs

Jᴜsᴛ Fᴏʀᴡᴀʀᴅ A Mᴇssᴀɢᴇ ᴏʀ Mᴇᴅɪᴀ Tᴏ Sᴛᴀʀᴛ

Pᴏᴡᴇʀᴅ Bʏ : @AIOM_BOTS</b>
"""


REPLY_MARKUP = InlineKeyboardMarkup(
               [[
               InlineKeyboardButton("Sᴇᴛᴛɪɴɢs", callback_data="captz")
               ],[     
               InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
               InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about")
               ],[
               InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")
               ]]
               )


@Client.on_message(filters.command("start"))
async def start(client, msg):
    fuser = msg.from_user.id
    if check_blacklist(fuser):
        return
    add_chat(fuser)
    await msg.reply(
        text=START_MSG.format(msg.from_user.mention),
        reply_markup=REPLY_MARKUP,
        disable_web_page_preview=True
    )
