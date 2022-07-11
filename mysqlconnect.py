import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "film"
)

cursor = db.cursor()
sql = "Select * from classifyfilm"

cursor.execute(sql)
for (id, name, director, genre, classification) in cursor:
    print(name)