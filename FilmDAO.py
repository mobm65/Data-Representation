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
    sql = "insert into film (id, name, director, genre, classification) values (%s,%s,%s,%s,%s)"
    values = [
        film["id"], 
        film["name"], 
        film["director"], 
        film["genre"], 
        film["classification"]
        ]
    cursor.execute(sql, values)
    self.db.commit()
    return cursor.lastrowid

def getAll(self):
    cursor = self.db.cursor()
    sql = "select * from film"
    cursor.execute(sql)
    results=cursor.fetchall()
# store in array 
    returnArray = []
    for result in results:
        resultAsDict = self.converttoDict(result)
        returnArray.append(resultAsDict)
    
    return returnArray

def findByid(self, id):
    cursor = self.db.cursor()
    sql = "select * from film where id = %s"
    values = ["id"]
    cursor.execute(sql, values)
    result=cursor.fetchone()
    return self.convertToDict(result)




def update(self, film):
    cursor = self.db.cursor()
    sql = "update film set name = %s,  director =%s, genre = %s, classification = %s where id = %s"
    values = [
        film["name"], 
        film["director"], 
        film["genre"], 
        film["classification"],
        film["id"]
        ]
    cursor.execute(sql, values)
    self.db.commit()
    return film

def delete(self, id):
    cursor = self.db.cursor()
    sql = "delete from film where id = %s"
    values = ["id"]
    cursor.execute(sql, values)
    
    return{}

def convertToDict(self, result):
    colnames = ["id", "name", "director", "filmgenre", "filmclassification"]
    film = {}

    if result:
        for i , colname in enumerate(colnames):
            value = result[i]
            film[colname] = value
    return film        
FilmDAO = FilmDAO()

print("connection made")
