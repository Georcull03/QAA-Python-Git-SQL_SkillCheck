CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name VARCHAR(20) NOT NULL,
    drink_size VARCHAR(20) NOT NULL,
    extras VARCHAR(35),
    price FLOAT NOT NULL
);

INSERT INTO orders (customer_name, drink_size, price) VALUES ('Jerry', 'Medium', 6.50);
INSERT INTO orders (customer_name, drink_size, extras, price) VALUES ('Rebecca', 'Large', 'Whipped cream, Marshmallows', 9.10);