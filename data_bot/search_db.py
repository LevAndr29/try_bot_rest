import sqlite3
from contextlib import closing
from pathlib import Path
from json import loads


dir_path = Path.cwd()
data_b = str(Path(dir_path, 'restauran_data.db'))

def names_category():
    with closing(sqlite3.connect(data_b)) as file:
        with closing(file.cursor()) as cur:
            cur.execute(f"SELECT id_category, name_category FROM category;")
            search = cur.fetchall()
            if search is None or search[1] is None:
                return -1
            id_categ, name_categ = [], []
            for cat in search:
                id_categ.append(cat[0])
                name_categ.append(cat[1])
            return id_categ, name_categ
def id_names_dish(category=0):
    with closing(sqlite3.connect(data_b)) as file:
        with closing(file.cursor()) as cur:
            cur.execute(f"SELECT id_dish, dish_name FROM menu WHERE view={category};")
            search = cur.fetchall()
            if search is None:
                return -1
            id_dish, name_dish = [], []
            for cat in search:
                id_dish.append(cat[0])
                name_dish.append(cat[1])
            return id_dish, name_dish

def is_order(id_client, mode=0):
    with closing(sqlite3.connect(data_b)) as file:
        with closing(file.cursor()) as cur:
            cur.execute(f"SELECT order_now, number_table FROM tables WHERE id_client='{id_client}';")
            search = cur.fetchone()
            try:
                table = search[1]
                search = loads(search[0])
            except:
                return 'Вы ещё не добавили блюда'
            dishs = search['order']
            order = ''
            price = 0
            for dish in dishs:
                cur.execute(f"SELECT dish_name, price FROM menu WHERE id_dish={int(dish)};")
                search = cur.fetchone()
                order += search[0] + ' ' + search[1] + '\n'
                price += int(search[1])
            if mode == 1:
                text = 'Новый заказ:\n' + order + f'\nОбщая стоимость: {price}\nстолик: {table}'
                return text
            text = 'Ваш заказ:\n' + order + f'\nОбщая стоимость: {price}\nПодтвердить заказ?'
            return text
