# The service file interacts with the DB file to Query or Modify data within the database
# Typically there will be a function for each process that is required, and these will take in data and return data

import db

def get_all():
    data = db.view_all_records()
    return data

def read_by_id(id):
    query = f'SELECT * FROM orders WHERE order_id = {id};'
    data = db.run_query(query)
    return data 

def create_order(customer_name, drink_size, extras, price):
    query = f"INSERT INTO orders (customer_name, drink_size, extras, price) VALUES ('{customer_name}', '{drink_size}', '{extras}', {price});"
    db.run_query(query)
    return 'Order created'

def update_order(field, value, id):
    if isinstance(value, str):
        query = f"UPDATE orders SET {field} = '{value}' WHERE order_id = {id};"
    else:
        query = f"UPDATE orders SET {field} = {value} WHERE order_id = {id};"
    db.run_query(query)
    return 'Order updated'

def delete_order(id):
    query = f'DELETE FROM orders WHERE order_id = {id};'
    db.run_query(query)
    return True

def delete_all():
    query = 'DELETE FROM orders WHERE order_id > 0;'
    db.run_query(query)
    return True