import asyncio
import json
import sqlite3
from contextlib import closing
from pathlib import Path
from create_bot import error_stop
# from data_base.create_data import data_b, scrambler, find_role, id_all_room, number_game, decoder
import random



# id_role = json.dumps({'role1': 14, "role2": None})
# old_id_role = json.loads(search[0])


dir_path = Path.cwd()
data_b = str(Path(dir_path, 'restauran_data.db'))  #

def add_dish(dish_name, description, price, view, photo='zero'):
    with closing(sqlite3.connect(data_b)) as file:
        with closing(file.cursor()) as cur:
            cur.execute(f"SELECT * FROM menu WHERE '{dish_name}'=dish_name;")
            c = cur.fetchone()
            if c is None:
                cur.execute(f"SELECT * FROM menu;")
                count = len(cur.fetchall())
                photo = json.dumps({'photo': photo})
                data_dish = (count, dish_name, description, price, view, photo)
                cur.execute(f"INSERT INTO menu (id_dish, dish_name, description, price, view, json_menu) VALUES(?, ?, ?, ?, ?, ?);", data_dish)
                file.commit()
            else:
                return False
            return True


def add_menu():
    add_dish('рыба', 'рыбка на костре', 500, 1)
    add_dish('вода', 'вода без газа', 10, 2)
    add_dish('Борщ', 'свекольный суп', 10, 3)
    add_dish('Сок', 'апельсиновый сок', 10, 2)
    add_dish('Гречка', 'каша гречневая', 10, 0)
    add_dish('Картофельное пюре', 'Картошка', 10, 0)
    print('Блюда добавлены')
add_menu()

def add_in_order(id_client, time, dish):
    with closing(sqlite3.connect(data_b)) as file:
        with closing(file.cursor()) as cur:
            cur.execute(f"SELECT order_now FROM tables WHERE id_client='{id_client}';")
            try:
                order_now = json.loads(cur.fetchone()[0])
            except:
                return 'Вначале выберите столик.'
            order_now['order'].append(dish)
            order_now['time'] = time
            # print(order_now)
            order_now = json.dumps(order_now)
            cur.execute(f"UPDATE tables SET order_now='{order_now}' "
                        f"WHERE id_client='{id_client}';")
            file.commit()
            return 'Блюдо добавлено'

def add_order(id_client, times):
    with closing(sqlite3.connect(data_b)) as file:
        with closing(file.cursor()) as cur:
            cur.execute(f"SELECT order_now FROM tables WHERE id_client='{id_client}';")
            order_now = json.loads(cur.fetchone()[0])
            order_all = order_now['order']
            print(order_all)
            cur.execute(f"SELECT * FROM order_tab;")
            id_order = len(cur.fetchall())
            data = times['data']
            time = times['time']
            cur.execute(f"SELECT number_table FROM tables WHERE id_client='{id_client}';")
            table = int(cur.fetchone()[0])
            order_all = json.dumps(order_all)
            data_order = (id_order, data, time, table, order_all)
            cur.execute(f"INSERT INTO order_tab (id_order, data, time, tabl, ordere) "
                        f"VALUES(?, ?, ?, ?, ?);", data_order)
            cur.execute(f"SELECT order_now FROM tables WHERE number_table={table};")
            order_now = json.loads(cur.fetchone()[0])
            order_now['order'] = []
            order_now = json.dumps(order_now)
            cur.execute(f"UPDATE tables SET order_now='{order_now}' "
                    f"WHERE number_table={table};")
            cur.execute(f"UPDATE tables SET id_client=NULL "
                        f"WHERE number_table={table};")
            file.commit()
            return 'Заказ составлен'

def change_id_client_table(id_client, table):
    with closing(sqlite3.connect(data_b)) as file:
        with closing(file.cursor()) as cur:
            if id_client == 0:
                cur.execute(f"SELECT order_now FROM tables WHERE number_table={table};")
                order_now = json.loads(cur.fetchone()[0])
                order_now['order'] = []
                order_now = json.dumps(order_now)
                cur.execute(f"UPDATE tables SET order_now='{order_now}' "
                        f"WHERE number_table={table};")
                cur.execute(f"UPDATE tables SET id_client=NULL "
                            f"WHERE number_table={table};")
                file.commit()
                return 'Столик очищен'
            cur.execute(f"SELECT id_client FROM tables WHERE number_table={table};")
            id_cli = cur.fetchone()
            print(id_cli)
            try:
                if id_cli[0] is not None:
                    return 'Этот столик занят'
            except:
                return 'Этот столик занят'
            try:
                cur.execute(f"UPDATE tables SET id_client='{id_client}' "
                        f"WHERE number_table={table};")
            except:
                cur.execute(f"SELECT number_table FROM tables WHERE id_client='{id_client}';")
                return f'Вы уже сидите за {cur.fetchone()[0]} столом.\nХотите поменять?'
            file.commit()
            return 'Прошу, садитесь!'
