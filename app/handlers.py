from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


import random

import app.keyboards as kb
import app.bd as bd


router = Router()


@router.message(F.photo)
async def photo_handler(message: Message):
    photo_data = message.photo[-1]
    await message.answer(f'{photo_data}')

@router.message(CommandStart())
async def start(message: Message):
    await message.answer_photo("AgACAgIAAxkBAAIBx2c0ygYD_UtTsd64fcymqflrFex0AAJd4jEbrVqoSZfttvYHTU5CAQADAgADeQADNgQ",
                               caption=bd.StartText,
                               reply_markup=kb.main)


@router.message(F.text == 'Скучаю')
async def miss(message: Message):
    await message.answer_photo(random.choice(bd.image), caption=random.choice(bd.i_miss),
                               reply_markup=kb.main)


@router.message(F.text == 'Я люблю тебя')
async def love(message: Message):
    await message.answer_photo(random.choice(bd.image), caption=random.choice(bd.i_love_you),
                               reply_markup=kb.main)


@router.message(F.text == 'Хочу тебя')
async def want(message: Message):
    await message.answer_photo(random.choice(bd.image), caption=random.choice(bd.want_you),
                         reply_markup=kb.main)


@router.message(F.text == 'Ты меня любишь?')
async def do_you(message: Message):
    await message.answer_photo(random.choice(bd.image), caption=random.choice(bd.do_you_love_me),
                         reply_markup=kb.main)


@router.message()
async def how_are_you(message: Message):
    await message.answer("Зайка, я не понимаю что ты говоришь, может как сильно любишь меня, или какую то фигню, но я могу ответить одно, я люблю тебя",
                         reply_markup=kb.main)