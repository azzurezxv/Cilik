import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Afffaantuhhhh.events import register
from Afffaantuhhhh import telethn as tbot
from Afffaantuhhhh import BOT_USERNAME as bu

PHOTO = "https://telegra.ph/file/72991fad3de48ba4e02fb.jpg"

@register(pattern=("/alive"))
async def awake(event):
  JHON = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Miku.** \n\n"
  JHON += "✪ **I'm Working Properly** \n\n"
  JHON += f"✪ **My Master : [Jhon](https://t.me/Afffaantuhhhh)** \n\n"
  JHON += f"✪ **Library Version :** `{telever}` \n\n"
  JHON += f"✪ **Telethon Version :** `{tlhver}` \n\n"
  JHON += f"✪ **Pyrogram Version :** `{pyrover}` \n\n"
  BUTTON = 🔥Thanks For Adding Me🔥**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", f"https://t.me/{bu}?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​","https://t.me/azzurezxv")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=JHON,  buttons=BUTTON)
