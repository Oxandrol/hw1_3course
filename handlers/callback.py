from config import dp,bot
from aiogram import types , Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@dp.callback_query_handler( text="quiz_1_button",)
async def quiz_2(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton("NEXT", callback_data="quiz_2_button")
    markup.add(button_2, )


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
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type="quiz",
        correct_option_id=4,
        explanation="Дурачок была же подсказка",
        open_period=10,
        reply_markup=markup
    )

@dp.callback_query_handler( text="quiz_2_button",)
async def quiz_3(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_3 = InlineKeyboardButton("NEXT", callback_data="quiz_3_button")
    markup.add(button_3, )

    question = "Спутник земли ?"
    answer = [
        "Луна",
        "ХЗ",
        "Марс",
        "Солце",
        "Я",
        "Ночью светит",
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type="quiz",
        correct_option_id=0,
        explanation="Ночью светит чё",
        open_period=10,
        reply_markup=markup
    )

@dp.callback_query_handler( text="quiz_3_button",)
async def quiz_4(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_4 = InlineKeyboardButton("NEXT", callback_data="quiz_4_button")
    markup.add(button_4, )

    question = "FullStack and Backend это одни и тоже ?"
    answer = [
        "Да",
        "Нет",
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type="quiz",
        correct_option_id=1,
        explanation="Нет",
        open_period=10,
        reply_markup=markup
    )

@dp.callback_query_handler( text="quiz_4_button",)
async def quiz_5(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_5 = InlineKeyboardButton("NEXT", callback_data="quiz_5_button")
    markup.add(button_5, )

    question = "DC OR MARVEL ?"
    answer = [
        "DC",
        "MARVEL",
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type="quiz",
        correct_option_id=1,
        explanation="None",
        open_period=10,
        reply_markup=markup
    )

def register_handler_callback(dp: Dispatcher):
    dp.register_message_handler(quiz_2,text="quiz_1_button")
    dp.register_message_handler(quiz_3, text="quiz_2_button")
    dp.register_message_handler(quiz_4, text="quiz_3_button")
    dp.register_message_handler(quiz_5, text="quiz_4_button")