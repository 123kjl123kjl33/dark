from pyrogram import Client, filters
from pyrogram.types import Message
from YukkiMusic import app
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


@app.on_message(
    command(["السورس", "سورس", "المبرمج"])
)
async def mak(client: Client, message: Message):
    await message.reply_photo(
        photo="https://envs.sh/6EK.jpg",
        caption="~ Team \n~ 𝖬𝗎𝗌𝗂𝖼 𝖱𝗂𝗆𝖺𝗌 𓏺 ميوزك الريماس",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⦗ Dev ⦘", url="https://t.me/V777G"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "⦗ Updates ⦘", url="https://t.me/F_FF6F"
                    ),
                    InlineKeyboardButton(
                        "⦗ support ⦘", url="https://t.me/BBSI8"
                    ),
                ],
            ]
        ),
    )
