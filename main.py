from aiogram.utils import executor
from config import dp
import logging

from handlers import client
from handlers import callback
from handlers import admin
# from handlers import extra

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
callback.register_handler_callback(dp)

# extra.register_handler_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

