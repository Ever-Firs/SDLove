from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='Скучаю'),
        KeyboardButton(text='Я люблю тебя')
        ],
        [
        KeyboardButton(text='Хочу тебя'),
        KeyboardButton(text='Ты меня любишь?')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Дорогая, выбирай!'
)