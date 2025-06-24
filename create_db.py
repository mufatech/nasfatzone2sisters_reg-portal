
import pg8000
from pg8000 import OperationalError

# Database connection parameters
DB_HOST = 'ep-empty-wind-a8vrahe8-pooler.eastus2.azure.neon.tech'
DB_USER = 'nasfat_sister_owner'
DB_PASSWORD = 'npg_Q0yKJgSV2UZH'
DB_NAME = 'nasfat_sister'

# DB_HOST = 'dpg-cq7pkqdds78s73dbd020-a.oregon-postgres.render.com'
# DB_USER = 'nasfat_render_user'
# DB_PASSWORD = 's4UqmMqfhJVnNBlLn8s0KdUowOrYklkE'
# DB_NAME = 'nasfat_render'

# Establish connection
try:
    connection = pg8000.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME
    )
    connection.autocommit = True

    # Create a cursor object
    cursor = connection.cursor()

    # Execute SQL query to create a database
    cursor.execute(f"CREATE DATABASE {DB_NAME}")

    print(f"Database '{DB_NAME}' created successfully!")

except OperationalError as e:
    print(f"Error connecting to PostgreSQL: {e}")

finally:
    # Close the cursor and connection
    if 'connection' in locals():
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

# import mysql.connector

# mydb = mysql.connector.connect(
#     host= 'dpg-cq7pkqdds78s73dbd020-a.oregon-postgres.render.com',
#     user= 'nasfat_render_user',
#     passwd = 's4UqmMqfhJVnNBlLn8s0KdUowOrYklkE',
# )

# my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE nasfat_render")

# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)
    
    
#     import mysql.connector

# mydb = mysql.connector.connect(
#     host= 'localhost',
#     user= 'mufatech',
#     passwd = 'mufatech',
# )

# my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE nasfat2")

# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)