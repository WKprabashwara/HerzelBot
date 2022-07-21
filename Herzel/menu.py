from Herzel import bot as app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from Herzel.utils.lang import *


fbuttons = InlineKeyboardMarkup(
        [
        [
          InlineKeyboardButton(text="📻 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐠𝐫𝐨𝐮𝐩", url="https://t.me/Herzelsup_GroUp"),
          InlineKeyboardButton(text="💬 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐜𝐡𝐚𝐧𝐧𝐞𝐥", url="https://t.me/HerzelUpdates")
        ],
        [ 
          InlineKeyboardButton(text="📍𝐂𝐫𝐞𝐝𝐢𝐭", callback_data='credit'),
          InlineKeyboardButton(text="❔𝐇𝐨𝐰 𝐭𝐨 𝐮𝐬𝐞 ", callback_data='htouse')
        ],
        [ 
          InlineKeyboardButton(text="📜 𝐒𝐨𝐮𝐫𝐜𝐞 𝐜𝐨𝐝𝐞", url="https://github.com/WKprabashwara/HerzelBot"),
          InlineKeyboardButton(text="📓 𝐃𝐨𝐜𝐮𝐦𝐞𝐧𝐭𝐚𝐭𝐢𝐨𝐧", url="https://prabashwarar.github.io")
        ], 
        [
          InlineKeyboardButton(text="✅ 𝐇𝐨𝐰 𝐭𝐨 𝐝𝐞𝐩𝐥𝐨𝐲 𝐌𝐞 . . .", url="https://prabashwarar.github.io")
        ],
        [
          InlineKeyboardButton("« 𝐁𝐚𝐜𝐤", callback_data='startcq')
        ]])

ckeyboard = InlineKeyboardMarkup(
        [
        [
          InlineKeyboardButton(text="📻 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐠𝐫𝐨𝐮𝐩", url="https://t.me/Herzelsup_GroUp"),
          InlineKeyboardButton(text="💬 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐜𝐡𝐚𝐧𝐧𝐞𝐥", url="https://t.me/HerzelUpdates")
        ],
        [ 
          InlineKeyboardButton(text="📍𝐂𝐫𝐞𝐝𝐢𝐭", callback_data='startcq'),
          InlineKeyboardButton(text="📍𝐂𝐫𝐞𝐝𝐢𝐭", callback_data='startcq')
        ],
        [ InlineKeyboardButton(text="📜 𝐒𝐨𝐮𝐫𝐜𝐞 𝐜𝐨𝐝𝐞", url="https://github.com/WKprabashwara/HerzelBot"),
          InlineKeyboardButton(text="📓 𝐃𝐨𝐜𝐮𝐦𝐞𝐧𝐭𝐚𝐭𝐢𝐨𝐧", url="https://prabashwarar.github.io")
        ], 
        [
          InlineKeyboardButton(text="✅ 𝐇𝐨𝐰 𝐭𝐨 𝐝𝐞𝐩𝐥𝐨𝐲 𝐌𝐞 . . .", url="https://prabashwarar.github.io")
        ],
        [
          InlineKeyboardButton("« 𝐁𝐚𝐜𝐤", callback_data='startcq')
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
     [InlineKeyboardButton("« 𝐁𝐚𝐜𝐤", callback_data='startcq')]])

@app.on_callback_query(filters.regex("_langs"))
@languageCB
async def commands_callbacc(client, CallbackQuery, _):
    await CallbackQuery.message.edit(
        text= "𝐂𝐡𝐨𝐨𝐬𝐞 𝐘𝐨𝐮𝐫 𝐥𝐚𝐧𝐠𝐮𝐚𝐠𝐞𝐬 :",
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

