import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="system",
    password="Admin123"
)
if mydb.connect:
    print("CONNECTED")