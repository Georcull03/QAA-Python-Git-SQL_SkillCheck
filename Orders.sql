CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name VARCHAR(20) NOT NULL,
    drink_size VARCHAR(20) NOT NULL,
    extras VARCHAR(35),
    price INT NOT NULL
)

INSERT INTO orders (customer_name, drink_size, price) VALUES ('Jerry', 'Medium', 6.50);
INSERT INTO orders (fish_eaten, penguin_name) VALUES ('Rebecca', 'Large', 'Whipped cream, Marshmallows');