from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from decouple import config

import logging





TOKEN = config("TOKEN")

bot = Bot(token=TOKEN)
dp =  Dispatcher(bot=bot)

@dp.message_handler(commands=['mem'])
async def process_photo_command(message: types.Message):
    with open("photo.jpg", 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo = photo)


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="quiz_1_button")
    markup.add(button_1)

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


@dp.callback_query_handler(text="quiz_1_button")
async def quiz_2(call: types.CallbackQuery):
    question = "Кто написал Евгений Онегин ?"
    answer = [
        "Никита Михалков",
        "Путин",
        "Лев Толстой",
        "ХЗ",
        "Пушкин",
        "Александр Сергеевич",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type="quiz",
        correct_option_id=4,
        explanation="Дурачок была же подсказка",
        open_period=10,
    )

@dp.message_handler()
async def message_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=message.text)
    try:
        number = int(message.text)
        result = number ** 2
        await message.answer(str(result))
        await message.reply("Это число которое возводится в квадрат!")
    except ValueError:
        pass


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=message.text)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)


