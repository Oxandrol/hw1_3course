import aiohttp
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from main import *


url = 'https://ru.sputnik.kg/latest_news/'

async def get_latest_news():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return []
            html = await resp.text()
            soup = BeautifulSoup(html, 'html.parser')
            headlines = soup.find_all('a', {'class': 'b-plainlist__item__title'})
            links = [a.get('href') for a in headlines]
            titles = [a.text for a in headlines]
            return [{'title': title, 'link': link} for title, link in zip(titles[:5], links[:5])]

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я буду отправлять тебе последние новости с sputnik.kg. Напиши /news, чтобы получить новости.")

@dp.message_handler(commands=['news'])
async def send_news(message: types.Message):
    latest_news = await get_latest_news()
    if not latest_news:
        await message.reply("К сожалению, не удалось получить последние новости.")
        return
    # Send the news to the user
    for news in latest_news:
        await bot.send_message(message.chat.id, f"{news['title']}\n{news['link']}")

def register_handlers_news(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(send_welcome, commands=['news'])


