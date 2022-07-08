import json
from pathlib import Path
import sqlite3



dir_path = Path.cwd()
data_b = str(Path(dir_path, 'restauran_data.db'))
def create_datas():
    try:
        file = sqlite3.connect(data_b)  # Создание или подключение к бд
        cur = file.cursor()
    except:
        print('База уже открыта (ошибка)')
    if file:
        print('Data base connected OK!')
    file.execute('''CREATE TABLE IF NOT EXISTS "order_tab" ("id_order"	INTEGER NOT NULL UNIQUE,	"data"	TEXT NOT NULL,	
                       "time"	TEXT NOT NULL, "tabl"	INTEGER NOT NULL, "ordere"	TEXT NOT NULL, "json_order"	TEXT);''')
    file.execute('''CREATE TABLE IF NOT EXISTS "menu" ("id_dish"	INTEGER NOT NULL UNIQUE,	"dish_name"	TEXT NOT NULL,	
                       "price"	TEXT NOT NULL, "description"    TEXT NOT NULL, 
                       "view"	INTEGER NOT NULL, "json_menu"	TEXT);''')
    file.execute('''CREATE TABLE IF NOT EXISTS "admin" ("id_admin"	INTEGER NOT NULL UNIQUE,	"tables"	TEXT NOT NULL,	
                       "json_admin"	TEXT);''')
    file.execute('''CREATE TABLE IF NOT EXISTS "types_dish" ("id_type"	INTEGER NOT NULL UNIQUE,	"name"	TEXT NOT NULL,	
                       "json_type"	TEXT);''')
    file.execute('''CREATE TABLE IF NOT EXISTS "tables" ("number_table"	INTEGER NOT NULL UNIQUE,	"order_now"	TEXT NOT NULL,	
                       "json_table"	TEXT,	"id_client"	TEXT);''')
    file.execute('''CREATE TABLE IF NOT EXISTS "category" ("id_category"	INTEGER NOT NULL,	
                        "name_category"	TEXT NOT NULL UNIQUE,   "json_category"	TEXT);''')
    file.commit()
    file.close()
create_datas()
def add_tables(num):
    try:
        file = sqlite3.connect(data_b)  # Создание или подключение к бд
        cur = file.cursor()
    except:
        print('База уже открыта (ошибка)')
    order = json.dumps({'order': [], 'officiant': 11111111})
    data_dish = (num, order)
    try:
        cur.execute(f"INSERT INTO tables (number_table, order_now) VALUES(?, ?);", data_dish)
    except:
        pass
    file.commit()
    file.close()

def add_category(name_category):
    try:
        file = sqlite3.connect(data_b)  # Создание или подключение к бд
        cur = file.cursor()
    except:
        print('База уже открыта (ошибка)')
    cur.execute(f"SELECT * FROM category;")
    num = len(cur.fetchall())
    data_category = (num, name_category)
    try:
        cur.execute(f"INSERT INTO category (id_category, name_category) VALUES(?, ?);", data_category)
    except:
        pass
    file.commit()
    file.close()
def add_cat():
    add_category('Гарниры')
    add_category('Горячее')
    add_category('Напитки')
    add_category('Супы')
add_cat()
tables = 4
for i in range(1, tables + 1):
    add_tables(i)