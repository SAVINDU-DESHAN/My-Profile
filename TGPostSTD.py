import os
import pytz
import asyncio
import datetime
import random
from pyrogram import filters, Client
from pyrogram.errors import FloodWait
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

#-------------Variables--------------
# Fill This Arias With Correct Values
APPID = "4875414"
APIHASH = "ecf8c1d5835af69a4040ba117ff96476"
BOTTOKEN = "6676691749:AAHI69AVFKTx_Hwa9ppzh-iaBRgtfCKLpV0"
CHANNEL_ID = -1001987738113
MESSAGE_ID = 3
TIME_ZONE = "Asia/Colombo"
# Not Recommended to Change Other Things Of Code.




poststd = Client(
   "tgpoststd",
   api_id=APPID,
   api_hash=APIHASH,
   bot_token=BOTTOKEN,
)

@poststd.on_callback_query(filters.regex("timeshow_"))
async def time(_, query: CallbackQuery):
              TimeZone_Std = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
              Time_Std = TimeZone_Std.strftime("%I:%M %p")
              Date_Std = TimeZone_Std.strftime("%B %d") 
              timetxt = f"☘️Now Time\n\n⏰Time: {Time_Std}\n📅Date: {Date_Std}\nTime Zone: {TIME_ZONE}\n\nPowered by☘️\n@Savindu_deshan"
              await poststd.answer_callback_query(query.id, text=timetxt, show_alert=True)

@poststd.on_callback_query(filters.regex("rescpet_"))
async def stats_callbacc(_, CallbackQuery):
    text = "🚀Resctpet Sri Lanka People..."
    await poststd.answer_callback_query(CallbackQuery.id, text, show_alert=False)

async def main_sithijatd():
    async with poststd:
            while True:
              TimeZone_Std = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
              Time_Std = TimeZone_Std.strftime("%I:%M %p")
              Date_Std = TimeZone_Std.strftime("%Y %B %d - %A")
              await poststd.edit_message_reply_markup(int(CHANNEL_ID),
              MESSAGE_ID,
              reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"🇱🇰 SriLanka", callback_data="rescpet_")
                ],
                [
                    InlineKeyboardButton(f"🗓 {Date_Std}", callback_data="timeshow_"),
                    InlineKeyboardButton(f"⌚️ {Time_Std} ", callback_data="timeshow_")
                ],
                [
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_")
                ], 
                [
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_")
                ],
               [
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_")
                ],
                [
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_")
                ],
                [
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚧", callback_data="rescpet_"),
                   InlineKeyboardButton(f"🚦", callback_data="rescpet_")
                ],
                [
                    InlineKeyboardButton("💬Contract Me💬", user_id="@SAVINDU_DESHAN_BOT") 
                ],
                [
                    InlineKeyboardButton("🚧 Github 🚧", url="https://github.com/SAVINDU-DESHAN"),
                    InlineKeyboardButton("🚀Facebook🚀", url="https://www.facebook.com/Savindu.D.Vijayasingha")   
                ]
            ]))
              print("Time Updated!")
              await asyncio.sleep(60)

poststd.run(main_sithijatd())
