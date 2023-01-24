# The DB file contains the processes and functions to create our Database or connect to it as well as run the initial SQL
# The DB file should also contain query functions that the Service file can use to read or modify the data

import sqlite3 as sql

conn = sql.connect('QACafe-db')

cursor = conn.cursor()

def setup_table():
    sql_file = open('Orders.sql')
    sql_string = sql_file.read()
    cursor.executescript(sql_string)

def run_query(query):
    data = cursor.execute(query).fetchall()
    return data

def view_all_records():
    query = 'SELECT * FROM orders;'
    data = run_query(query)
    return data

def create_order(customer_name, drink_size, extras, price):
    query = f"INSERT INTO orders (customer_name, drink_size, extras, price) VALUES ('{customer_name}', '{drink_size}', '{extras}', {price});"
    run_query(query)
    return True

def commit_changes():
    conn.commit()


# setup_table()

# create_order("George", "Small", "Marshmallows, Vanilla", 4.10)
print(view_all_records())

conn.commit()

