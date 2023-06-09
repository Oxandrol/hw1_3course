from aiogram.utils import executor

import logging


from config import dp, bot, ADMINS

from new_func import news
from handlers import client
from handlers import callback
from handlers import admin
from handlers import fsmadmin
from handlers import schedule
from database.bot_db import sql_create
# from database.bot_db import sql_create
# from handlers import extra
news.register_handlers_news(dp)
fsmadmin.register_handlers_fsm(dp)

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
callback.register_handler_callback(dp)



async def on_startup(dp):
    await schedule.set_sheduler()
    sql_create()
    await bot.send_message(ADMINS[0], "Я родился!")


async def on_shutdown(dp):
    await bot.send_message(ADMINS[0], "Пока пока!")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)

