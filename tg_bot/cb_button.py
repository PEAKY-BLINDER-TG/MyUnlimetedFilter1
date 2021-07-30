from pyrogram import filters
from pyrogram import Client as MT_ID_Bot
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from mt_id_bot.text.cmd_text import START_MSG, HELP_MSG, ABOUT_MSG, ID_MSG, INFO_MSG
from mt_id_bot.button.cb_button import CB_START, CB_HELP, CB_ABOUT
from mt_id_bot.button.cmd_button import BACK_BUTTON

@MT_ID_Bot.on_callback_query(filters.regex(r"^(start|help|about|id|info|close)$"))
async def callback_data(mt_id_bot, update: CallbackQuery):

    query_data = update.data

    if query_data == "start":
    
        reply_markup = CB_START
        
        await update.message.edit_text(
            START_MSG,
            reply_markup=reply_markup,
            parse_mode="html",
            disable_web_page_preview=True
        )
