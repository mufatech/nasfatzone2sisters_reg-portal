
import pg8000
from pg8000 import OperationalError

# Establish connection
DB_HOST = 'ep-shiny-dust-ajfzqvgr-pooler.c-3.us-east-2.aws.neon.tech'
DB_USER = 'neondb_owner'
DB_PASSWORD = 'npg_Pu9N6bqEDaSV'
DB_NAME = 'nasfatsister_regportal'


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