import sqlite3 as sq
from itertools import product


def initiate_db():
    with sq.connect('products_data.db') as con:
        cur = con.cursor()

        cur.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL)
        ''')

        cur.execute("""
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NO NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL DEFAULT 1000)
        """)

def get_all_products():
    with sq.connect('products_data.db') as con:
        cur = con.cursor()

        cur.execute('SELECT * FROM Products')
        products = cur.fetchall()

    return products

def add_user(username, email, age):
    with sq.connect('products_data.db') as con:
        cur = con.cursor()

        cur.execute("INSERT INTO Users (username, email, age) VALUES(?, ?, ?)", (username, email, age))

def is_included(username):
    with sq.connect('products_data.db') as con:
        cur = con.cursor()

        cur.execute("SELECT username FROM Users WHERE username == ?", (username,))
        user = cur.fetchone()
        return user is not None