import mysql.connector

mydb = mysql.connector.connect(
    host= 'dpg-cq7pkqdds78s73dbd020-a.oregon-postgres.render.com',
    user= 'nasfat_render_user',
    passwd = 's4UqmMqfhJVnNBlLn8s0KdUowOrYklkE',
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE nasfat_render")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
    
    
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