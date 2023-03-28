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

# 3 Select all data from the table Order Details and descriptive statistics for the Order Details table
order_details = pd.read_sql_query("SELECT * FROM `Order Details`", c)
print(order_details)
print(order_details.describe())

# 4 Select all data from the table categories and descriptive statistics for the categories table
categories = pd.read_sql_query("SELECT * FROM categories", c)
print(categories)
print(categories.describe())

# 5 Select all data from the table customers and descriptive statistics for the customers table
customers = pd.read_sql_query("SELECT * FROM customers", c)
print(customers)
print(customers.describe())

# 6 Select o.OrderID ,o.CustomerID, o.EmployeeID, o.OrderDate, o.ShipAddress, o.CompanyName, c.ContactName, c.Phone, c.Country from orders o inner join customers c on order.CustomerID = customers.CustomerID
order_customer = pd.read_sql_query("SELECT o.OrderID, o.CustomerID, o.EmployeeID, o.OrderDate, o.ShipAddress, c.CompanyName, c.ContactName, c.Phone, c.Country FROM orders o INNER JOIN customers c ON o.CustomerID = c.CustomerID;", c)
print(order_customer)
print(order_customer.describe())

# Complete


# Count Country in order_customer and sort by Country show the result [Country, number of orders]
order_customer_country = order_customer.groupby('Country').count()
# change name header OrderID to number of orders
order_customer_country.rename(columns={'OrderID': 'Number of Orders'}, inplace=True)
# Show Country and number of orders
print(order_customer_country[['Number of Orders']])


order_customer_country.describe()
print(order_customer_country[['Number of Orders']].describe())
