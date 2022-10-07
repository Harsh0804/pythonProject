import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin123"
)

if mydb.is_connected():
    print("connected")
else:
    print("not connected")