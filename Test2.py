import sqlite3 as sql
import pandas as pd

# Connect to the database
c = sql.connect("northwind.db")

# List all tables in the database
list_table = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", c)
print(list_table)

# 1 Select all data from the table products and descriptive statistics for the products table
products = pd.read_sql_query("SELECT * FROM products", c)
print(products)
print(products.describe())

# 2 Select all data from the table orders and descriptive statistics for the orders table
orders = pd.read_sql_query("SELECT * FROM orders", c)

print(orders)

print(orders.describe())
