import asyncio
import importlib
import re
from contextlib import closing, suppress
from uvloop import install
from pyrogram import filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from Herzel.menu import *
from Herzel import *
from Herzel.plugins import ALL_MODULES
from Herzel.utils import paginate_modules
from lang import get_command
from Herzel.utils.lang import *
from Herzel.utils.commands import *
from Herzel.mongo.rulesdb import *
from Herzel.utils.start import *
from Herzel.utils.kbhelpers import *
from Herzel.mongo.usersdb import *
from Herzel.mongo.restart import *
from Herzel.mongo.chatsdb import *
from Herzel.plugins.fsub import ForceSub
import random

loop = asyncio.get_event_loop()
flood = {}
START_COMMAND = get_command("START_COMMAND")
HELP_COMMAND = get_command("HELP_COMMAND")
HELPABLE = {}

async def start_bot():
    global HELPABLE
    for module in ALL_MODULES:
        imported_module = importlib.import_module("Herzel.plugins." + module)
        if (
            hasattr(imported_module, "__MODULE__")
            and imported_module.__MODULE__
        ):
            imported_module.__MODULE__ = imported_module.__MODULE__
            if (
                hasattr(imported_module, "__HELP__")
                and imported_module.__HELP__
            ):
                HELPABLE[
                    imported_module.__MODULE__.replace(" ", "_").lower()
                ] = imported_module
    all_module = ""
    j = 1
    for i in ALL_MODULES:
        if j == 1:
            all_module += "•≫ Successfully imported:{:<15}.py\n".format(i)
            j = 0
        else:
            all_module += "•≫ Successfully imported:{:<15}.py".format(i)
        j += 1           
    restart_data = await clean_restart_stage()
    try:
        if restart_data:
            await app.edit_message_text(
                restart_data["chat_id"],
                restart_data["message_id"],
                "**Restarted Successfully**",
            )

        else:
            await app.send_message(-1001749160500, "**Deployed Successfully ! \n\n (C) 2021-2022 by @ImPrabashwara :)**")
	
    except Exception:
        pass
    print(f"{all_module}")
    print("""
 _____________________________________________   
|                                             |  
|          Deployed Successfully              |  
|       (C) 2021-2022 by @ImPrabashwara       | 
|        Greetings from Prabashwara  :)       |
|_____________________________________________|""")
    await idle()

    await aiohttpsession.close()
    await app.stop()
    for task in asyncio.all_tasks():
        task.cancel() 



home_keyboard_pm = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="➕ 𝐀𝐝𝐝 𝐦𝐞 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩 ➕",
                url=f"http://t.me/{BOT_USERNAME}?startgroup=new",
            )
        ],
        [
           InlineKeyboardButton(
                text="ℹ️ 𝐀𝐛𝐨𝐮𝐭", callback_data="_about"
            ),
            InlineKeyboardButton(
                text="🌏 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞𝐬", callback_data="_langs"
            ),
        ],
        [
	    InlineKeyboardButton(
		text="👨‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫",
		url="https://t.me/Imprabashwara"
	    ),
            InlineKeyboardButton(
                text="⚙️ 𝐇𝐞𝐥𝐩", callback_data="bot_commands"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌐 𝐖𝐞𝐛𝐬𝐢𝐭𝐞",
                url=f"https://prabashwarar.github.io",
            ),
            InlineKeyboardButton(
                text="⚜️ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐜𝐡𝐚𝐧𝐧𝐞𝐥",
                url=f"https://t.me/HerzelUpdates",
            )
        ],
    ]
)

keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="📚 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 & 𝐇𝐞𝐥𝐩",
                url=f"t.me/{BOT_USERNAME}?start=help",
            )
        ]
    ]
)

@app.on_message(filters.command(START_COMMAND))
@language
async def start(client, message: Message, _):
    FSub = await ForceSub(bot, message)
    if FSub == 400:
        return
    chat_id = message.chat.id
    if message.chat.type != "private":
        await message.reply(
            _["main2"], reply_markup=keyboard)
        await adds_served_user(chat_id)     
        return await add_served_chat(chat_id) 
    if len(message.text.split()) > 1:
        name = (message.text.split(None, 1)[1]).lower()
        if name.startswith("rules"):
                await get_private_rules(app, message, name)
                return     
        if name.startswith("learn"):
                await get_learn(app, message, name)
                return     
        if "_" in name:
            module = name.split("_", 1)[1]
            text = (_["main6"].format({HELPABLE[module].__MODULE__}
                + HELPABLE[module].__HELP__)
            )
            await message.reply(text, disable_web_page_preview=True)
        if name == "help":
            text, keyb = await help_parser(message.from_user.first_name)
            await message.reply(
                _["main5"],
                reply_markup=keyb,
                disable_web_page_preview=True,
            )
        if name == "connections":
            await message.reply("𝐑𝐮𝐧 /connections 𝐭𝐨 𝐯𝐢𝐞𝐰 𝐨𝐫 𝐝𝐢𝐬𝐜𝐨𝐧𝐧𝐞𝐜𝐭 𝐟𝐫𝐨𝐦 𝐠𝐫𝐨𝐮𝐩𝐬 !")
    else:
	await app.send_sticker(message.chat.id,"CAACAgUAAxkBAAIi6GLYrVxLGp_qSAjHyE_uraTIWcUqAAJyBQAC0jnJVpnSmrnRyfzuHgQ")
        await message.reply(f"""
𝐇𝐞𝐲 {message.from_user.mention} 𝐈'𝐦 𝐇𝐞𝐫𝐳𝐞𝐥 🥀. 
𝐈 𝐜𝐚𝐧 𝐡𝐞𝐥𝐩 𝐦𝐚𝐧𝐚𝐠𝐞 𝐲𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩 𝐰𝐢𝐭𝐡 𝐮𝐬𝐞𝐟𝐮𝐥 𝐟𝐞𝐚𝐭𝐮𝐫𝐞𝐬, 𝐅𝐞𝐞𝐥 𝐟𝐫𝐞𝐞 𝐭𝐨 𝐚𝐝𝐝 𝐦𝐞 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩 ! 📻 𝐈'𝐦 𝐦𝐚𝐝𝐞 𝐛𝐲 @TeamHerzel 💸

𝐇𝐢𝐭 /help 𝐭𝐨 𝐟𝐢𝐧𝐝 𝐦𝐲 𝐥𝐢𝐬𝐭 𝐨𝐟 𝐚𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬 🔑
""",reply_markup=home_keyboard_pm)
        return await add_served_user(chat_id) 


@app.on_message(filters.command(HELP_COMMAND))
@language
async def help_command(client, message: Message, _):
    FSub = await ForceSub(bot, message)
    if FSub == 400:
        return
    if message.chat.type != "private":
        if len(message.command) >= 2:
            name = (message.text.split(None, 1)[1]).replace(" ", "_").lower()
            if str(name) in HELPABLE:
                key = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text=_["main3"],
                                url=f"t.me/{BOT_USERNAME}?start=help_{name}",
                            )
                        ],
                    ]
                )
                await message.reply(
                    _["main4"],
                    reply_markup=key,
                )
            else:
                await message.reply(
                    _["main2"], reply_markup=keyboard
                )
        else:
            await message.reply(
                _["main2"], reply_markup=keyboard
            )
    else:
        if len(message.command) >= 2:
            name = (message.text.split(None, 1)[1]).replace(" ", "_").lower()
            if str(name) in HELPABLE:
                text = (_["main6"].format({HELPABLE[name].__MODULE__}
                + HELPABLE[name].__HELP__)
                )
                if hasattr(HELPABLE[name], "__helpbtns__"):
                       button = (HELPABLE[name].__helpbtns__) + [[InlineKeyboardButton("« 𝐁𝐚𝐜𝐤", callback_data="bot_commands")]]
                if not hasattr(HELPABLE[name], "__helpbtns__"): button = [[InlineKeyboardButton("« 𝐁𝐚𝐜𝐤", callback_data="bot_commands")]]
                await message.reply(text,
                           reply_markup=InlineKeyboardMarkup(button),
                           disable_web_page_preview=True)
            else:
                text, help_keyboard = await help_parser(
                    message.from_user.first_name
                )
                await message.reply(
                    _["main5"],
                    reply_markup=help_keyboard,
                    disable_web_page_preview=True,
                )
        else:
            text, help_keyboard = await help_parser(
                message.from_user.first_name
            )
            await message.reply(
                text, reply_markup=help_keyboard, disable_web_page_preview=True
            )
    return
  
@app.on_callback_query(filters.regex("startcq"))
@languageCB
async def startcq(client,CallbackQuery, _):
    served_chats = len(await get_served_chats())
    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    served_users = len(await get_served_users())
    served_users = []
    users = await get_served_users()
    for user in users:
        served_users.append(int(user["bot_users"]))
    await CallbackQuery.message.edit(
            text=f"""
**𝐇𝐞𝐲** {CallbackQuery.from_user.mention} **𝐈'𝐦 𝐇𝐞𝐫𝐳𝐞𝐥 🥀. 
𝐈 𝐜𝐚𝐧 𝐡𝐞𝐥𝐩 𝐦𝐚𝐧𝐚𝐠𝐞 𝐲𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩 𝐰𝐢𝐭𝐡 𝐮𝐬𝐞𝐟𝐮𝐥 𝐟𝐞𝐚𝐭𝐮𝐫𝐞𝐬, 𝐅𝐞𝐞𝐥 𝐟𝐫𝐞𝐞 𝐭𝐨 𝐚𝐝𝐝 𝐦𝐞 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩 ! 📻 𝐈'𝐦 𝐦𝐚𝐝𝐞 𝐛𝐲 @TeamHerzel 💸**

**𝐇𝐢𝐭** /help **𝐭𝐨 𝐟𝐢𝐧𝐝 𝐦𝐲 𝐥𝐢𝐬𝐭 𝐨𝐟 𝐚𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬 🔑**
""",disable_web_page_preview=True,reply_markup=home_keyboard_pm)


async def help_parser(name, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    return (
"""**𝐌𝐚𝐢𝐧  𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬 : [🥀](https://telegra.ph/file/f55e6422e731172dca376.png)**

• 𝐈'𝐦 𝐚 𝐠𝐫𝐨𝐮𝐩 𝐦𝐚𝐧𝐚𝐠𝐞𝐦𝐞𝐧𝐭 𝐛𝐨𝐭 𝐰𝐢𝐭𝐡 𝐬𝐨𝐦𝐞 𝐮𝐬𝐞𝐟𝐮𝐥 𝐟𝐞𝐚𝐭𝐮𝐫𝐞𝐬.
• 𝐘𝐨𝐮 𝐜𝐚𝐧 𝐜𝐡𝐨𝐨𝐬𝐞 𝐚𝐧 𝐨𝐩𝐭𝐢𝐨𝐧 𝐛𝐞𝐥𝐨𝐰, 𝐛𝐲 𝐜𝐥𝐢𝐜𝐤𝐢𝐧𝐠 𝐚 𝐛𝐮𝐭𝐭𝐨𝐧.
• 𝐈𝐟 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐚𝐧𝐲 𝐛𝐮𝐠𝐬 𝐨𝐫 𝐪𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐨𝐧 𝐡𝐨𝐰 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞, 
• 𝐡𝐚𝐯𝐞 𝐚 𝐥𝐨𝐨𝐤 𝐚𝐭 𝐦𝐲 [𝐃𝐨𝐜𝐬](https://szsupunma.gitbook.io/herzel-bot/), 𝐨𝐫 𝐡𝐞𝐚𝐝 𝐭𝐨 @ImPrabashwara.

**𝐀𝐥𝐥 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐜𝐚𝐧 𝐛𝐞 𝐮𝐬𝐞𝐝 𝐰𝐢𝐭𝐡 𝐭𝐡𝐞 𝐟𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠: /**""",keyboard,)

@app.on_message(filters.command("ads"))
async def ads_message(_, message):
	await app.forward_messages(
		chat_id = message.chat.id, 
		from_chat_id = int(-1001356358215), 
		message_ids = 2255,
	)

@app.on_callback_query(filters.regex("bot_commands"))
@languageCB
async def commands_callbacc(client,CallbackQuery, _):
    text ,keyboard = await help_parser(CallbackQuery.from_user.mention)
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=_["main5"],
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()

@app.on_callback_query(filters.regex(r"help_(.*?)"))
@languageCB
async def help_button(client, query, _):
    home_match = re.match(r"help_home\((.+?)\)", query.data)
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    create_match = re.match(r"help_create", query.data)
    top_text = _["main5"]
    if mod_match:
        module = (mod_match.group(1)).replace(" ", "_")
        text = (
            "{} **{}**:\n".format(
                "𝐇𝐞𝐫𝐞 𝐢𝐬 𝐭𝐡𝐞 𝐡𝐞𝐥𝐩 𝐟𝐨𝐫", HELPABLE[module].__MODULE__
            )
            + HELPABLE[module].__HELP__
            + "\n👨‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 : @ImPrabashwara"
        )
        if hasattr(HELPABLE[module], "__helpbtns__"):
                       button = (HELPABLE[module].__helpbtns__) + [[InlineKeyboardButton("« 𝐁𝐚𝐜𝐤", callback_data="bot_commands")]]
        if not hasattr(HELPABLE[module], "__helpbtns__"): button = [[InlineKeyboardButton("« 𝐁𝐚𝐜𝐤", callback_data="bot_commands")]]
        await query.message.edit(
            text=text,
            reply_markup=InlineKeyboardMarkup(button),
            disable_web_page_preview=True,
        )
        await query.answer(f"𝐇𝐞𝐫𝐞 𝐢𝐬 𝐭𝐡𝐞 𝐡𝐞𝐥𝐩 𝐟𝐨𝐫 {module}")
    elif home_match:
        await app.send_message(
            query.from_user.id,
            text= _["main2"],
            reply_markup=home_keyboard_pm,
        )
        await query.message.delete()
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif back_match:
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif create_match:
        text, keyboard = await help_parser(query)
        await query.message.edit(
            text=text,
            reply_markup=keyboard,
            disable_web_page_preview=True,
        )

    return await client.answer_callback_query(query.id)

if __name__ == "__main__":
    install()
    with closing(loop):
        with suppress(asyncio.exceptions.CancelledError):
            loop.run_until_complete(start_bot())
        loop.run_until_complete(asyncio.sleep(3.0)) 
