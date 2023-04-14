from config import dp,bot
from aiogram import types , Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@dp.message_handler(commands=['mem'])
async def process_photo_command(message: types.Message):
    with open("photo.jpg", 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo = photo)


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="quiz_1_button")
    markup.add(button_1,)

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

def register_handlers_client(dp:Dispatcher):
    dp.register_message_handler(process_photo_command, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
