import string, json
from pathlib import Path
from aiogram.dispatcher.filters import Text
import time, datetime
# from data_base.choise_db import search_room, plus_randoms, id_from_room, del_player
# from data_base.search_db import player_in_room
from data_bot.change_db import add_in_order, add_order, change_id_client_table
from data_bot.search_db import is_order
from handlers import reply_key as Keyboard
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from create_bot import bot

class Dish(StatesGroup):
    step_one = State()
    step_two = State()
    step_table = State()
    start_time = State()
    step_player = State()

async def cmd_start(message: types.Message):
    flag = 0  # сделать проверку админ или нет если нет, то 0
    await message.answer(f'Здравствуйте!\nЧто бы вы хотели?', reply_markup=Keyboard.key(flag))

async def new_dish(message: types.Message, state: FSMContext):
    flag = 0  # сделать проверку админ или нет если нет, то 0
    # print(str(message.date))
    print(message.from_user.id)
    await Dish.step_one.set()
    await message.answer(f'Выберите категорию:', reply_markup=Keyboard.choise_category())
async def after_category(query: types.CallbackQuery, state: FSMContext):
    category = query.data.lower()
    await bot.send_message(query.from_user.id, f'Что бы вы хотели:', reply_markup=Keyboard.key_dish(int(category[8:])))
    await query.message.delete()
    await Dish.step_two.set()

async def add_dish_table(query: types.CallbackQuery, state: FSMContext):
    dish = query.data.lower()
    time_order = str(query.message.date)
    time_date = {}
    time_date['data'] = time_order[:10]
    time_date['time'] = time_order[11:16]
    print(add_in_order(id_client=query.from_user.id, time=time_date, dish=dish))
    print(query.from_user.id)
    await bot.send_message(query.from_user.id, f'Блюдо добавлено')
    await query.message.delete()
    await state.finish()

async def new_order(message: types.Message):
    time_order = str(message.date)
    time_date = {}
    time_date['data'] = time_order[:10]
    time_date['time'] = time_order[11:16]
    # print(time_date)
    # print(is_order(message.from_user.id))
    await message.answer(is_order(message.from_user.id), reply_markup=Keyboard.yes_no_key())
async def order_add(query: types.CallbackQuery):
    time_order = str(query.message.date)
    time_date = {}
    time_date['data'] = time_order[:10]
    time_date['time'] = time_order[11:16]
    await bot.send_message(1024144209, is_order(query.from_user.id, mode=1))
    await bot.send_message(query.from_user.id, add_order(id_client=query.from_user.id, times=time_date))
    await query.message.delete()
async def you_right(query: types.CallbackQuery):
    await bot.send_message(query.from_user.id, 'Ваше право')
    await query.message.delete()

async def choise_table(message: types.Message):
    await message.answer(f'Выберите столик:', reply_markup=Keyboard.choise_table())
    await Dish.step_table.set()
async def client_table(query: types.CallbackQuery, state: FSMContext):
    text = query.data.lower()
    print(text, 'text')
    await bot.send_message(query.from_user.id, change_id_client_table(id_client=query.from_user.id, table=int(text)))
    await query.message.delete()
    await state.finish()
def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(new_dish, Text(equals="Добавить блюдо", ignore_case=True), state="*")
    dp.register_message_handler(choise_table, Text(equals="Выбрать столик", ignore_case=True), state="*")
    dp.register_callback_query_handler(order_add, Text(equals="order_add", ignore_case=True), state="*")
    dp.register_callback_query_handler(you_right, Text(equals="false", ignore_case=True), state="*")
    dp.register_message_handler(new_order, Text(equals="Сделать заказ", ignore_case=True), state="*")
    dp.register_callback_query_handler(after_category, state=Dish.step_one)
    dp.register_callback_query_handler(add_dish_table, state=Dish.step_two)
    dp.register_callback_query_handler(client_table, state=Dish.step_table)



    # dp.register_callback_query_handler(del_pers2, Text(equals=delet, ignore_case=True), state="*")
    # dp.register_message_handler(del_pers, commands="del_pers", state="*")
    # dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
    # dp.register_message_handler(cmd_room, commands="rooms", state="*")
    # dp.register_message_handler(buy_games, commands="buy_games", state="*")
    # dp.register_message_handler(add_people, commands="add", state="*")
    # # dp.register_errors_handler(error_bot_blocked)
    # dp.register_message_handler(filter_mat, state="*")