from config import dp, bot
from aiogram import types, Dispatcher


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


# @dp.message_handler()
# async def echo(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id, text=message.text)


def register_handler_extra(dp: Dispatcher):
    dp.register_message_handler(message_handler)
