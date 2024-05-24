from bot import dp, bot
from aiogram.utils import executor
from config import BOT_ADMIN
from handlers.users.default_user_handlers import register_user_handlers
from utils.dbms import create_tables





async def bot_start(_):
    bot_info = await bot.get_me()
    name = bot_info['first_name']
    await bot.send_message(BOT_ADMIN, f'''Бот {name} запущен!▶''')
    create_tables()

async def bot_stop(_):
    bot_info = await bot.get_me()
    name = bot_info['first_name']
    await bot.send_message(BOT_ADMIN, f'''Бот {name} остановлен!🛑''')

register_user_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=bot_start, on_shutdown=bot_stop)