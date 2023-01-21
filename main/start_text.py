from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from config import PREMUIM_USER
from script import Script
 

@Client.on_message(filters.command("start") & filters.private)                             
async def start_cmd(bot, msg):
    txt=Script.START_TXT.format(msg.from_user.mention),
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("Help", callback_data="help"),
        InlineKeyboardButton("About", callback_data="about")
        ],[
        InlineKeyboardButton("Exit", callback_data="close")
    ]])
    await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)
    return


@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):   
    txt=Script.START_TXT,
    button= [[
        InlineKeyboardButton("Help", callback_data="help"),
        InlineKeyboardButton("About", callback_data="about")
        ],[
        InlineKeyboardButton("Exit", callback_data="close") 
    ]]  
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt=Script.HELP_TXT,
    button= [[        
        InlineKeyboardButton("Purchase Plan", callback_data="plan_upgrade"),
        ][
        InlineKeyboardButton("FAQ", url="https://rishiee.me/rename-bot-FAQ"),
        InlineKeyboardButton("Back", callback_data="start")
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)


@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    text=Script.ABOUT_TXT,
    reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("Exit", callback_data="close")
        ]]
    )

@Client.on_callback_query(filters.regex("close"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return


# @Client.on_message(filters.command("Plan"))
# async def plan(bot, msg):
#     user = msg.from_user.id
#     if user not in :
 #        await msg.reply_text(f"{msg.from_user.id} Dear user you are currently not subscribed to any plans. Please upgrade a plan to use this bot.")
 #    else:
   #      await msg.reply_text(
  # #           "Plan Details Will be added soon."
   # # #      )
