import os
import logging

# Импорты фремворка
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Импорт для скрытия Токена
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('BOT_TOKEN'),)

dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
count_but = KeyboardButton('Рассчитать')
info_but = KeyboardButton('Информация')
kb.add(count_but, info_but)
# kb.add(info_but)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def cmd_start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text="Рассчитать")
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age_user=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth_user=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def set_calories(message, state):
    await state.update_data(weight_user=message.text)
    data = await state.get_data()
    calorie = 10 * int(data['weight_user']) + 6.25 * int(data['growth_user']) - 5 * int(data['age_user']) + 5
    await message.answer(f'Количество калорий: {calorie}ккал в день для оптимального похудения.')
    await state.finish()
#
# @dp.message_handler()
# async def all_massages(message):
#     await message.answer('Введите команду /start, чтобы начать общение.')
#     # print('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
