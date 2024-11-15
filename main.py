import asyncio

from aiogram import Bot, Dispatcher, types

from dotenv import load_dotenv
import os
from app.handlers import router

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
    ])

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)