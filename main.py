from bot import dp, bot
from aiogram.utils import executor
from config import BOT_ADMIN



bot_info = await bot.get_me()
name = bot_info['first_name']

async def bot_start(_):
    await bot.send_message(BOT_ADMIN, f'''Бот {name} запущен!▶''')

async def bot_stop(_):
    await bot.send_message(BOT_ADMIN, f'''Бот {name} остановлен!🛑''')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=bot_start, on_shutdown=bot_stop)