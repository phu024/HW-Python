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

# create_connection("northwind.db")

c = create_connection("northwind.db")


# Create a table
def create_table(table_name):
    """ create a table from the given database table name """
    c.execute('''CREATE TABLE IF NOT EXISTS {} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price REAL
            )'''.format(table_name))
    conn.commit()
    print("Table {} created".format(table_name))
    return c

# Insert data into the table
def insert_data(table_name, df):
    """ insert a dataframe into the given table """
    df.to_sql(table_name, con=c, if_exists='replace', index=False)
    print("Dataframe {} inserted".format(table_name))
    return c

# Select all data from the table
def select_all_data(table_name):
    """ select all data from the given table """
    df = pd.read_sql_query("SELECT * FROM {}".format(table_name), c)
    return df

# Select_all_data by id
def select_data_by_id(table_name, id):
    """ select data from the given table by id """
    df = pd.read_sql_query("SELECT * FROM {} WHERE id = {}".format(table_name, id), c)
    return df

# Delete data from the table by id
def delete_data(table_name, id):
    """ delete data from the given table by id """
    df = pd.read_sql_query("DELETE FROM {} WHERE id = {}".format(table_name, id), c)
    return df

# Update data in the table by id
def update_data(table_name, id, df):
    """ update data in the given table by id """
    df.to_sql(table_name, con=c, if_exists='replace', index=False)
    print("Dataframe {} updated".format(table_name))
    return c


conn = create_connection("northwind.db")

# Select all data from the products table

products = select_all_data("products")
print(products)

# Descriptive statistics for the products table

print(products.describe())