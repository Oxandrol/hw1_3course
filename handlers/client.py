from config import dp, bot
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import bot
from .client_kb import start_markup
from database.bot_db import sql_command_random, sql_command_all_users, sql_command_insert_user
from .utils import get_ids_from_users

from paser.parser import parser


async def start_command(message: types.Message):
    users = await sql_command_all_users()
    ids = get_ids_from_users(users)
    if message.from_user.id not in ids:
        await sql_command_insert_user(
            message.from_user.id,
            message.from_user.username,
            message.from_user.full_name
        )
    await bot.send_message(message.from_user.id, f"Салалекум {message.from_user.full_name}",
                           reply_markup=start_markup)


async def help_command(message: types.Message):
    await message.reply("Сам разбирайся!")


@dp.message_handler(commands=['mem'])
async def process_photo_command(message: types.Message):
    with open("photo.jpg", 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo)


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="quiz_1_button")
    markup.add(button_1, )

    question = "Когда была земельно-водная реформа на Севере Кыргызстана?"
    answer = [
        "Весна 1921 года",
        "Зима 1930 года",
        "Осень 1941",
        "Лето 1488 года",

    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type="quiz",
        correct_option_id=0,
        explanation="На истории Кыргызстана бы убили",
        open_period=10,
        reply_markup=markup
    )
    # await message.answer_poll()


async def get_series(message: types.Message):
    size = message.text.split()[-1] \
        if len(message.text.split()) == 2 else None
    movies: list[dict] = parser(size)
    for movies in movies:
        await message.answer_photo(
            photo=movies['image'],
            caption=f"{movies['url']}\n\n"
                    f"{movies['title']}\n"
                    f"{movies['rating']}\n"
                    f"#Y{movies['description']} "
        )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(process_photo_command, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(get_series, commands=['series'])
