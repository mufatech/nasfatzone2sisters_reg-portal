import psycopg2

# Establish connection
DB_HOST = 'ep-empty-wind-a8vrahe8-pooler.eastus2.azure.neon.tech'
DB_USER = 'nasfat_sister_owner'
DB_PASSWORD = 'npg_Q0yKJgSV2UZH'
DB_NAME = 'nasfat_sister'

# Establish connection
try:
    connection = psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME
    )
    connection.autocommit = True

    # Create a cursor object
    cursor = connection.cursor()

    # Example query
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Connected to PostgreSQL server, version: {db_version}")

except psycopg2.OperationalError as e:
    print(f"Error connecting to PostgreSQL: {e}")

finally:
    # Close the cursor and connection
    if 'connection' in locals():
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

# import psycopg2

# # Establish connection
# DB_HOST = 'dpg-cq7pkqdds78s73dbd020-a.oregon-postgres.render.com'
# DB_USER = 'nasfat_render_user'
# DB_PASSWORD = 's4UqmMqfhJVnNBlLn8s0KdUowOrYklkE'
# DB_NAME = 'nasfat_render'

# # Establish connection
# try:
#     connection = psycopg2.connect(
#         host=DB_HOST,
#         user=DB_USER,
#         password=DB_PASSWORD,
#         dbname=DB_NAME
#     )
#     connection.autocommit = True

#     # Create a cursor object
#     cursor = connection.cursor()

#     # Example query
#     cursor.execute("SELECT version();")
#     db_version = cursor.fetchone()
#     print(f"Connected to PostgreSQL server, version: {db_version}")

# except psycopg2.OperationalError as e:
#     print(f"Error connecting to PostgreSQL: {e}")

# finally:
#     # Close the cursor and connection
#     if 'connection' in locals():
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")

# import mysql.connector

# # Establish connection
# connection = mysql.connector.connect(
#     # host= 'localhost',
#     # user= 'mufatech',
#     # passwd = 'mufatech',
#     # database= 'nasfat2'
# )


# Create cursor
# cursor = connection.cursor()

# # Execute SQL query
# cursor.execute("SHOW TABLES")

# # Fetch and display results
# tables = cursor.fetchall()
# for table in tables:
#     print(table[0])

# # Close the cursor and connection
# cursor.close()
# connection.close()
