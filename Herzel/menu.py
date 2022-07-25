from Herzel import bot as app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from Herzel.utils.lang import *


fbuttons = InlineKeyboardMarkup(
        [
        [
          InlineKeyboardButton(text="📻 Suppor Group", url="https://t.me/Herzelsup_GroUp"),
          InlineKeyboardButton(text="💬 Support Channel", url="https://t.me/HerzelUpdates")
        ],
        [ 
          InlineKeyboardButton(text="📍Credit", callback_data='credit'),
          InlineKeyboardButton(text="❔How to use Me ", callback_data='htouse')
        ],
        [ 
          InlineKeyboardButton(text="📜 Source Code", url="https://github.com/WKprabashwara/HerzelBot"),
          InlineKeyboardButton(text="📓 Documentation", url="https://prabashwarar.github.io")
        ], 
        [
          InlineKeyboardButton(text="✅ How to Deploy Me . . .", url="https://telegra.ph/How-to-Develop-herzel-Bot-07-25")
        ],
        [
          InlineKeyboardButton("« Back", callback_data='startcq')
        ]])

ckeyboard = InlineKeyboardMarkup(
        [
        [
          InlineKeyboardButton(text="📻 Suppor Group", url="https://t.me/Herzelsup_GroUp"),
          InlineKeyboardButton(text="💬 Support Channel", url="https://t.me/HerzelUpdates")
        ],
        [ 
          InlineKeyboardButton(text="📍Credit", callback_data='credit'),
          InlineKeyboardButton(text="❔How to use Me ", callback_data='htouse')
        ],
        [ 
          InlineKeyboardButton(text="📜 Source Code", url="https://github.com/WKprabashwara/HerzelBot"),
          InlineKeyboardButton(text="📓 Documentation", url="https://prabashwarar.github.io")
        ], 
        [
          InlineKeyboardButton(text="✅ How to Deploy Me . . .", url="https://telegra.ph/How-to-Develop-herzel-Bot-07-25")
        ],
        [
          InlineKeyboardButton("« Back", callback_data='startcq')
        ]])

keyboard = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="🇱🇷 English", callback_data="languages_en")],
     [InlineKeyboardButton(text="🇱🇰 සිංහල", callback_data="languages_si"), 
      InlineKeyboardButton(text="🇮🇳 हिन्दी", callback_data="languages_hi")], 
     [InlineKeyboardButton(text="🇮🇹 Italiano", callback_data="languages_it"), 
      InlineKeyboardButton(text="🇮🇳 తెలుగు", callback_data="languages_ta")], 
     [InlineKeyboardButton(text="🇮🇩 Indonesia", callback_data="languages_id"), 
      InlineKeyboardButton(text="🇦🇪 عربي", callback_data="languages_ar")], 
     [InlineKeyboardButton(text="🇮🇳 മലയാളം", callback_data="languages_ml"), 
      InlineKeyboardButton(text="🇲🇼 Chichewa", callback_data="languages_ny")], 
     [InlineKeyboardButton(text="🇩🇪 German", callback_data="languages_ge"), 
      InlineKeyboardButton(text="🇷🇺 Russian", callback_data="languages_ru")], 
     [InlineKeyboardButton("« Back", callback_data='startcq')]])

@app.on_callback_query(filters.regex("_langs"))
@languageCB
async def commands_callbacc(client, CallbackQuery, _):
    await CallbackQuery.message.edit(
        text= "Choose your language :",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    
@app.on_callback_query(filters.regex("_about"))
@languageCB
async def commands_callbacc(client, CallbackQuery, _):
    await CallbackQuery.message.edit(
        text=_["menu"],
        reply_markup=fbuttons,
        disable_web_page_preview=True,
    )

@app.on_callback_query(filters.regex("_credit"))
@languageCB
async def commands_callbacc(client, CallbackQuery, _):
    await CallbackQuery.message.edit(
        text= "credit :",
        reply_markup=ckeyboard,
        disable_web_page_preview=True,
    )

