# The controller acts as the API for the app, in this case it will exist as a terminal based app
# using inputs and if statements to specify what the app should do

# It will run commands from the service file, which in turn uses the DB file to 
# query and create data and will return the data back to the user

from service import *
import db

def start_app():
    print(start_menu)
    exit = False
    while not exit:
        choice = int(input('Please choose a mode to continue: '))
        if choice == 1:
            print(create_orders())
        elif choice == 2:
            print(read_id())
        elif choice == 3:
            print(read_all())
        elif choice == 4:
            print(update_an_order())
        elif choice == 5:
            print(delete_order())
        elif choice == 6:
            print(delete_all())
        else:
            exit = True
            db.commit_changes()

def create_orders():
    cust_name = input('Please enter the customer name: ')
    drink_size = input('Please enter the drink size: ')
    extras = input('Please enter any extras: ')
    price = float(input('Please enter the price of the drink: '))
    return create_order(cust_name, drink_size, extras, price)

def read_all():
    return get_all()

def read_id():
    id = input('Please enter an order id to read: ')
    return read_by_id(id)

def update_an_order():
    column = input('Please enter a column you would like to update: ')
    replacement_value = input('Please enter data: ')
    id = input('Please enter the order id you would like to update: ')
    return update_order(column, replacement_value, id)

start_menu = """
    Welcome to the QA Cafe, what would you like to do? 

    1. Create an order
    2. Read an order by ID
    3. Read all Orders
    4. Update an order
    5. Delete an order
    6. Delete all orders
    7. Exit
    """


# print(get_all())
start_app()