import os
import logging

# Импорты фремворка
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, Message

# Импорт для скрытия Токена
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
import crud_functions

# Инициализация базы данных
crud_functions.initiate_db()

bot = Bot(token=os.getenv('BOT_TOKEN'),)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
count_but = KeyboardButton('Рассчитать')
info_but = KeyboardButton('Информация')
buy_but = KeyboardButton('Купить')
register_but = KeyboardButton('Регистрация')
kb.add(count_but, info_but)
kb.add(buy_but, register_but)

inline_kb = InlineKeyboardMarkup(resize_keybord=True)
count_inl = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
formul_inl = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb.add(count_inl, formul_inl)

ikb_product = InlineKeyboardMarkup(resize_keyboard=True)
p1_inl = InlineKeyboardButton(text="Product1", callback_data="product_buying")
p2_inl = InlineKeyboardButton(text="Product2", callback_data="product_buying")
p3_inl = InlineKeyboardButton(text="Product3", callback_data="product_buying")
p4_inl = InlineKeyboardButton(text="Product4", callback_data="product_buying")
ikb_product.add(p1_inl, p2_inl)
ikb_product.add(p3_inl, p4_inl)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username =State()
    email = State()
    age = State()
    # balance = State()

@dp.message_handler(commands=['start'])
async def cmd_start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)



@dp.message_handler(text='Рассчитать')
async def main_menu(message: Message):
    await message.answer('Выберите опцию', reply_markup=inline_kb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Для мужчин: 10 х вес(кг) + 6,25 x рост(см) – 5 х возраст(лет) + 5;')
    await call.answer()

@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
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

@dp.message_handler(text="Купить")
async def get_buying_list(message):
    products = crud_functions.get_all_products()
    for prod in products:
        await message.answer(f"Название: {prod[1]} | Описание: {prod[2]} | Цена: {prod[3]}")
        # await message.answer_photo(prod[4])
        await message.answer("Выберите продукт для покупки:", reply_markup=ikb_product)

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer("Введите имя пользователя(только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if crud_functions.is_included(username):
        await message.answer("Пользователь существует, введите другое имя:")
    else:
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        user_data = await state.get_data()
        username = user_data["username"]
        email = user_data["email"]

        crud_functions.add_user(username, email, age)

        await message.answer("Регистрация завершена! Ваш аккаунт создан.", reply_markup=kb)
        await state.finish()
    except ValueError:
        await message.answer("Пожалуйста, введите возраст числом:")

@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')
    # print('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

