data = []


def binary_search(list1, n):
    low = 0
    high = 100
    mid = 50
    while True:
        if mid < n:
            data.append(mid)
            low = mid
            mid = (low + high) // 2

        elif mid > n:
            data.append(mid)
            high = mid
            mid = (low + mid) // 2

        elif mid == n:
            data.append(mid)
            return "Программа остоновлена!"


print(binary_search(range(1, 101), 78), f"{data} Количество попыток - {len(data)}")

from random import randint


def bubble(array):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if array[j] > array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff


N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))

print(a)
bubble(a)
print(a)
# import sqlite3
#
#
# def create_connection(db_name):
#     connection = None
#     try:
#         connection = sqlite3.connect(db_name)
#     except sqlite3.Error as e:
#         print(e)
#     return connection
#
#
# def create_table(conn, sql):
#     try:
#         cursor = conn.cursor()
#         cursor.execute(sql)
#     except sqlite3.Error as e:
#         print(e)
#
#
# def insert_products(conn, products):
#     sql = '''
#     INSERT INTO products (product_title, price, quantity)
#     VALUES (?, ?, ?)'''
#     try:
#         cursor = conn.cursor()
#         cursor.execute(sql, products)
#         conn.commit()
#     except sqlite3.Error as e:
#         print(e)
#
#
# connect = create_connection('hw.db')
#
# sql_create_products_table = '''
# CREATE TABLE products (
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# product_title VARCHAR(200) NOT NULL,
# price DOUBLE(8, 2) NOT NULL DEFAULT 0.0,
# quantity INTEGER(5) NOT NULL DEFAULT 0
# )
# '''
#
# if connect is not None:
#     print('Connected successfully')
#     create_table(connect, sql_create_products_table)
#     insert_products('apple', (120, 99))
#
#     connect.close()