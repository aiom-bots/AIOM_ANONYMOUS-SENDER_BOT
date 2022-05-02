from pyrogram import Client
from vars import var

aiom = Client(
    "Anonymous-Sender",
    api_id=var.API_ID,
    api_hash=var.API_HASH,
    bot_token=var.BOT_TOKEN,
    plugins=dict(root="plugins"),
)

aiom.run()
