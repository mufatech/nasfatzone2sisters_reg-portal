import mysql.connector

# Establish connection
connection = mysql.connector.connect(
    host= 'dpg-cq7pkqdds78s73dbd020-a.oregon-postgres.render.com',
    user= 'nasfat_render_user',
    passwd = 's4UqmMqfhJVnNBlLn8s0KdUowOrYklkE',
    database= 'nasfat_render'
    # host= 'localhost',
    # user= 'mufatech',
    # passwd = 'mufatech',
    # database= 'nasfat2'
    
)

# Create cursor
cursor = connection.cursor()

# Execute SQL query
cursor.execute("SHOW TABLES")

# Fetch and display results
tables = cursor.fetchall()
for table in tables:
    print(table[0])

# Close the cursor and connection
cursor.close()
connection.close()
