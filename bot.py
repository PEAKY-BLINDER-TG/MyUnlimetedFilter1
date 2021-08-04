import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from files import UPDATE_CHANNEL

Motechyt = Client(
            "MT ID BOT",
            bot_token = os.environ["TOKEN"],
            api_id = int(os.environ["API_ID"]),
            api_hash = os.environ["API_HASH"]
)

# start and Update channel added
@Motechyt.on_message(filters.private & filters.command("start"))
async def start(bot, update):  

    text = f"""
<b> 👋Hello {update.from_user.mention}</b>
<b>I CAN GET ANY PUBLIC AND PRIVATE CHANNEL ID
FORWARD A MESSAGE FROM YOUR CHANNEL TO GET YOUR CHANNEL ID.
CLICK /ID GET YOUR ID
CLICK /INFO GET YOUR TELEGRAM INFO </b>
"""
    reply_markup =  MT_START
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
  )

# Button Controler 
MT_START = InlineKeyboardMarkup(
     [[
        InlineKeyboardButton("🗣️Group", url=f"t.me/mo_tech_group"),
        InlineKeyboardButton("📑Bot List", url=f"t.me/mo_tech_yt"),
        InlineKeyboardButton("✳️Source", url=f"https://github.com/PR0FESS0R-99/ID-Bot")
     ]]
   )
