import sqlite3

conn = sqlite3.connect('B&G.db')
c = conn.cursor()

c.execute("""CREATE TABLE ACCOUNT (
                ID text,
                PASS text,
                f_name text,
                l_name text,
                number text,
                address text
                )""")

c.execute("""CREATE TABLE CART (
                pic text,
                price integer,
                name text,
                ID text
                )""")

c.execute("""CREATE TABLE ORDERS (
                pic text,
                price integer,
                name text,
                f_name text,
                l_name text,
                number text,
                address text,
                ID text
                )""")

c.execute("""CREATE TABLE PRODUCTS (
                pic text,
                price integer,
                name text,
                catagory text,
                rate integer     
                )""")


conn.commit()
conn.close()