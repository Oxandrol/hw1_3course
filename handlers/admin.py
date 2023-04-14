from aiogram import Dispatcher, types
from config import bot, ADMINS
import random


async def game(message: types.Message):
    if message.from_user.id in ADMINS:
        emoji_list = ['⚽️', '🏀', '🎲', '🎯', '🎳', '🎰']
        r = random.choice(emoji_list)
        await bot.send_dice(message.chat.id, emoji=r)
    else:
        await bot.send_message(message.chat.id, 'Ты не мой господин')

async def pin(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMINS:
            await message.answer("Я не буду тебе приклоняться!")
        elif not message.reply_to_message:
            await message.answer('Только ответ на сообщение!!!!')
        else:
            await bot.pin_chat_message(
                message.chat.id,
                message.reply_to_message.message_id
            )
    else:
        await message.answer("Пиши в группе!")


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(game , commands=["dice"])
