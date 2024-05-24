from aiogram import types, Dispatcher
from bot import bot
from aiogram.dispatcher.filters.state import State, StatesGroup

async def command_start(message:types.Message):
    x = 8
    workday = 8
    for i in range(workday):
        if x==12:
            print(f'''Обед {x}''')
            x=x+1
        else:
            print(f'''{x}:00''')
            x=x+1


def register_user_handlers(dp:Dispatcher):
    dp.register_message_handler(command_start, commands='start')