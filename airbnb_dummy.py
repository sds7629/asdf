import random

import pymysql
from faker import Faker

fake = Faker()

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Rlawlsdn1573!",
    db="airbnb",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)


def generate_product_data(n):
    for _ in range(n):
        product_name = fake.word().capitalize() + " " + fake.word().capitalize()
        price = round(random.uniform(10, 100), 2)
        stock_quantity = random.randint(10, 100)
        create_date = fake.date_time_this_year()
        yield (product_name, price, stock_quantity, create_date)


def generate_customer_data(n):
    for _ in range(n):
        customer_name = fake.name()
        email = fake.email()
        address = fake.address()
        create_date = fake.date_time_this_year()
        yield (customer_name, email, address, create_date)


def generate_order_data(n, pks):
    for _ in range(n):
        pk = random.choice(pks)
        order_date = fake.date_time_this_year()
        total_amount = round(random.uniform(20, 500), 2)
        yield (pk, order_date, total_amount)


with conn.cursor() as cursor:
    products_sql = "INSERT INTO Products (productName, price, stockQuantity, craeteDate) VALUES (%s, %s, %s, %s)"
    for data in generate_product_data(10):
        cursor.execute(products_sql, data)
    conn.commit()

    customers_sql = "INSERT INTO Customers (customerName, email, address, createDate) VALUES (%s, %s, %s, %s)"
    for data in generate_customer_data(10):
        cursor.execute(customers_sql, data)
    conn.commit()

    cursor.execute("SELECT pk FROM customers")
    customer_ids = [row["pk"] for row in cursor.fetchall()]

    orders_sql = (
        "INSERT INTO orders (customerID, orderDate, totalAmount) VALUES (%s, %s, %s)"
    )
    for data in generate_order_data(15, customer_ids):
        cursor.execute(orders_sql, data)
    conn.commit()

conn.close()
