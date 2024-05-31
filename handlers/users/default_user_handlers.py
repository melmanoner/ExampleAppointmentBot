import datetime

from aiogram import types, Dispatcher
from bot import bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import json
import requests
from datetime import date, timedelta
from calendar import monthrange
#from keyboards.user.inlinekb import months_ikb
from aiogram_calendar import SimpleCalendar
from utils.other import get_months_duration

class AddWorktime(StatesGroup):
    welcome_msg = State()
    get_year_state = State()
    get_working_hours_state = State()
    get_lunch_hour_state = State()

async def command_start(message:types.Message):
    kb = await SimpleCalendar().start_calendar()
    await bot.send_message(message.from_user.id, 'Выберите дату', reply_markup=kb)
    x = get_months_duration()
    print(x)



async def add_worktime(message:types.Message):
    await bot.send_message(message.from_user.id, 'Ввдеите год который хотите заполнить:')
    await AddWorktime.get_year_state.set()

async def get_year(message:types.Message, state:FSMContext):
    year = message.text
    await state.update_data(year=year)
    await bot.send_message(message.from_user.id, 'Длительность рабочего дня?')
    await AddWorktime.get_working_hours_state.set()


async def get_working_hours(message:types.Message, state:FSMContext):
    working_hours = message.text
    await state.update_data(working_hours=working_hours)
    await bot.send_message(message.from_user.id, 'В каком часу у вас обед?')
    await AddWorktime.get_lunch_hour_state.set()

async def get_lunch_hour(message:types.Message, state:FSMContext):
    lunch = message.text
    data = await state.get_data()
    year = data['year']
    working_hours = ['working_hours']
    delta = timedelta(days=365)
    today = datetime.datetime.today()

    url = 'https://raw.githubusercontent.com/d10xa/holidays-calendar/master/json/consultant' + year + '.json'
    r = requests.get(url)
    cal = json.loads(r.text)
    print(cal["holidays"].count(""))



def register_user_handlers(dp:Dispatcher):
    dp.register_message_handler(command_start, commands='start')