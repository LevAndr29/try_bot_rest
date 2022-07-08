from aiogram.utils import executor  # для запуска в онлайн
from create_bot import dp
import logging

from data_bot.create_data import create_data
from handlers.client import register_handlers_common


async def on_startup(_):
    create_data()
    logging.basicConfig(
        # filename='errors.txt',
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    # Регистрация хэндлеров
    # register_handlers_room(dp)
    # register_call_bot(dp)
    # register_maf_blood(dp)
    # register_night_were(dp)
    register_handlers_common(dp)  # В конце, потому-что пустой
    await dp.start_polling()




executor.start_polling(dp, skip_updates=True,
                       on_startup=on_startup)