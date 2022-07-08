import mysql.connector

db = mysql.connector.connect(
    host = "localhost"
    user = "root"
    password = "root"
    database = "film"
)

cursor = db.cursor()
sql = "CREATE TABLE filmname (id INT NOT_NULL AUTO_INCREMENT, 
    name VARCHAR (250), diretor VARCHAR (250), id PRIMARY KEY)"

cursor.execute(sql)