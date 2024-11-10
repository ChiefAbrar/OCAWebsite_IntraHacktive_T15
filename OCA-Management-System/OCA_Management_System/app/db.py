#You will need it to connect the Python code to MySQL database.

import mysql.connector
from OCA_Management_System import db, app

db = mysql.connector.connect(host = "localhost", user="root", password="1234",database="oca_management_system", auth_plugin='mysql_native_password')
my_cursor = db.cursor()
my_cursor.execute("SHOW DATABASES LIKE 'oca_management_system'")
if my_cursor.fetchone() is None:
    my_cursor.execute("CREATE DATABASE oca_management_system")
    print("Database created successfully.")
else:
    print("Database already exists.")
for db in my_cursor:
    print(db)
my_cursor.close()
db.close()