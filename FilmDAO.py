import mysql.connector

class FilmDAO:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = "localhost"
            user = "root"
            password = "root"
            database = "film"
        )
        
def create(self, film):
    cursor = self.db.cursor()
    sql = "insert into film (id, name, director) values (%s,%s,%s)"
    values = [film["id"], film["name"], film["director"]]

    cursor.execute(sql, values)
    self.db.commit()
    return cursor.lastrowid

def getAll(self):
    cursor = self.db.cursor()
    sql = "select * from books"
    cursor.execute(sql)
    results=cursor.fetchall()
# store in array 
    returnArray = []
    print(results)


FilmDAO = FilmDAO()

print("connection made")
