import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "film"
)

# get database connection
def connect():
    return db

# test database connection
def main():
    cursor = db.cursor()
    sql = "Select * from classifyfilm"

    cursor.execute(sql)
    for (id, name, director, genre, classification) in cursor:
        print(name)

if __name__ == '__main__':
    main()
