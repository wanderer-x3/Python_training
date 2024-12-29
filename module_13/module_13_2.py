import asyncio
import os
import logging

# Импорты фремворка
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Импорт для скрытия Токена
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('BOT_TOKEN'),)

dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def cmd_start(message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
