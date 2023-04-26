import sqlite3
from sqlite3 import Error


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_product(conn, product):
    try:
        sql = '''INSERT INTO products (product_title, price, quantity) 
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_product_quantity(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def search_by_word(conn, word):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ('%' + word + '%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)


def update_product_price(conn, product):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_products(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        product_list = cursor.fetchall()
        for product in product_list:
            print(product)
    except sqlite3.Error as e:
        print(e)


def select_all_products_by_quantity_and_price(conn):
    try:
        sql = '''SELECT * FROM products WHERE quantity > 5 and price < 100.00'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print(rows)
    except sqlite3.Error as e:
        print(e)


connection = create_connection("hw.db")

create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0
)
'''

if connection is not None:
    print("Connected Success!")
    # create_table(connection, create_products_table)
    # insert_product(connection, ("Алькони", 78.2, 7))
    # insert_product(connection, ("Сосиски", 250.4, 26))
    # insert_product(connection, ("Колбаса", 300.5, 16))
    # insert_product(connection, ("Хлеб", 30.5, 50))
    # insert_product(connection, ("Сыр", 125.5, 25))
    # insert_product(connection, ("молоко", 15.5, 30))
    # insert_product(connection, ("Кефир", 50.5, 15))
    # insert_product(connection, ("Жвачка", 5.5, 10))
    # insert_product(connection, ("Чипсы", 220.5, 5))
    # insert_product(connection, ("Фанта", 85.5, 12))
    # insert_product(connection, ("Сырок", 85.5, 12))
    # insert_product(connection, ("Pepsi", 110.5, 12))
    # insert_product(connection, ("Сникерс", 30.6, 20))
    # insert_product(connection, ("Альбени", 27.3, 20))
    # insert_product(connection, ("Йогурт", 25.5, 10))

    # select_all_products(connection)
    # delete_products(connection, 14)
    # update_product_quantity(connection, (8, 7))
    # update_product_price(connection, (45, 1))
    # select_all_products(connection)
    connection.close()






