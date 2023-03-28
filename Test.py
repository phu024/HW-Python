import sqlite3
from sqlite3 import Error
import pandas as pd

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connected to database")
    except Error as e:
        print(e)
    return conn


# List all tables in the database

def list_tables(conn):
    """ List all tables in the database """
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()
    return tables

# Create a table
def create_table(table_name):
    """ create a table from the create_table_sql statement """
    sql_create_table = """CREATE TABLE IF NOT EXISTS {} (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        price real
                                    );""".format(table_name)
    c = conn.cursor()
    c.execute(sql_create_table)
    print("Table {} created".format(table_name))
    return c

# Select all data from the table
def select_all_data(table_name, conn):
    """ Query all rows in the table """
    df = pd.read_sql_query("SELECT * FROM {}".format(table_name), conn)
    return df

# Select_all_data by id
def select_data_by_id(table_name, id, conn):
    """ Query all rows in the table by id """
    c = conn.cursor()
    c.execute("SELECT * FROM {} WHERE id = {}".format(table_name, id))
    rows = c.fetchall()
    df = pd.DataFrame(rows)
    return df

# Delete data from the table by id
def delete_data(table_name, id, conn):
    """ Delete data from the table by id """
    c = conn.cursor()
    c.execute("DELETE FROM {} WHERE id = {}".format(table_name, id))
    print("Data deleted")
    return c


# Descriptive statistics for the table
def descriptive_statistics(table_name, conn):
    """ Descriptive statistics for the table """
    c = conn.cursor()
    c.execute("SELECT * FROM {}".format(table_name))
    rows = c.fetchall()
    df = pd.DataFrame(rows)
    return df.describe()



conn = create_connection("northwind.db")

# List all tables in the database
tables = list_tables(conn)
print(tables)

# Select all data from the products table

products = select_all_data("products", conn)
print(products)

#  Descriptive statistics for the products table
products_stats = descriptive_statistics("products", conn)
print(products_stats)
