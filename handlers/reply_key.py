from aiogram import types
from data_bot.search_db import names_category, id_names_dish

client = ["Сделать заказ", "Добавить блюдо", "Позвать официанта", "Выбрать столик"]

#inline
def choise_category(mode=0):
    add = 'category'
    id_category, name_categ = names_category()
    text_and_data = [(str(name_categ[0]), (add + str(id_category[0]))), ]
    for i in range(1, len(id_category)):
        text_and_data.append((str(name_categ[i]), (add + str(id_category[i]))))
    text_and_data = tuple(text_and_data)
    keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    keyboard_markup.add(*row_btns)
    return keyboard_markup
def key_dish(mode=0):
    id_dish, name_dish = id_names_dish(mode)
    text_and_data = []
    for i in range(len(id_dish)):
        text_and_data.append((str(name_dish[i]), (str(id_dish[i]))))
    text_and_data = tuple(text_and_data)
    keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    keyboard_markup.add(*row_btns)
    return keyboard_markup
def yes_no_key(mode=0):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)
    new_blood = (('1', '1'), )
    if mode == 0:
        new_blood = (
            ('👍🏽 Да', 'order_add'),
            ('👎🏽 Нет', 'False'),
        )
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in new_blood)
    keyboard_markup.add(*row_btns)
    return keyboard_markup

def choise_table():
    text_and_data = []
    for i in range(1, 4):
        text_and_data.append((str(i), (str(i))))
    text_and_data = tuple(text_and_data)
    keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    keyboard_markup.add(*row_btns)
    return keyboard_markup



#каллбек
def new_vamp(mode=0):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)
    new_blood = (('1', '1'), )
    if mode == 0:
        new_blood = (
            ('👍🏽 Да', 'True'),
            ('👎🏽 Нет', 'False'),
        )
    elif mode == 1:
        new_blood = (
            ('🧛‍♂️️Лорд', '16'),
            ('🧛‍♀️Королева', '17'),
            ('🧛🏾 Ревенант', '18'),
            ('🧛🏿‍♂️Князь', '19'),
            ('🧛🏻 Граф', '20'),
        )
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in new_blood)
    keyboard_markup.add(*row_btns)
    return keyboard_markup



# не колбек
def key(flag):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if flag == 0:
        for size in client:
            keyboard.add(size)
    else:
        pass
    return keyboard
