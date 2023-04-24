import asyncio
from datetime import datetime

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger
from apscheduler.triggers.interval import IntervalTrigger

from database.bot_db import sql_command_all_users
from config import bot


async def go_to_getup(bot: Bot):
    users = await sql_command_all_users()
    for user in users:
        await bot.send_message(user[0], f"Ну привет {user[-1]}\nПора в школу!")


async def set_sheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Astana")

    scheduler.add_job(go_to_getup, 'date', run_date=datetime(2023, 4, 26), args=['го в школу!'])

    scheduler.start()