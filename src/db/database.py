# database.py

import mysql.connector
from datetime import date
from src.db.config import DATABASE_CONFIG


def connect_to_db():
    return mysql.connector.connect(
        host=DATABASE_CONFIG['host'],
        user=DATABASE_CONFIG['user'],
        password=DATABASE_CONFIG['password'],
        database=DATABASE_CONFIG['database'],
        port=DATABASE_CONFIG['port']
    )


# Create a connection pool
connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="my_pool",
    pool_size=5,
    **DATABASE_CONFIG
)


def execute_query(query):

    connection = connection_pool.get_connection()
    cursor = connection.cursor()

    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result


def get_max_date():
    connection = connection_pool.get_connection()
    cursor = connection.cursor()

    query = "SELECT MAX(Hmeromnia) FROM anaplirotes ;" # Check table name from live server, might be different from local
    cursor.execute(query)
    result = cursor.fetchall()

    max_date = result[0][0] if result and result[0] and result[0][0] else None

#just for test, remove when want to use with real DB
    # max_date = date(2024, 10, 14)

    cursor.close()
    connection.close()

    return max_date
