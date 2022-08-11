from mysqlconnect import connect

# Data access for film
class FilmDAO:
    def __init__(self):
        self.db = connect()

    def create(self, film):
        cursor = self.db.cursor()
        sql = "insert into classifyfilm (name, director, filmgenre, filmclassification) values (%s,%s,%s,%s)"
        values = [
            film["name"],
            film["director"],
            film["filmgenre"],
            film["filmclassification"]
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from classifyfilm"
        cursor.execute(sql)
        results = cursor.fetchall()
        # store in array
        returnArray = []
        for result in results:
            resultAsDict = convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    # find film by id
    def findByid(self, id):
        cursor = self.db.cursor()
        sql = "select * from classifyfilm where id = %s"
        values = [id]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return convertToDict(result)

    # update film
    def update(self, film):
        cursor = self.db.cursor()
        sql = "update classifyfilm set name = %s,  director =%s, filmgenre = %s, filmclassification = %s where id = %s"
        values = [
            film["name"],
            film["director"],
            film["filmgenre"],
            film["filmclassification"],
            film["id"]
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return film

    # delete film
    def delete(self, id):
        cursor = self.db.cursor()
        sql = "delete from classifyfilm where id = %s"
        values = [id]
        cursor.execute(sql, values)
        self.db.commit()
        return{}

# Convert result from database to dict.
def convertToDict(result):
    colnames = ["id", "name", "director",
                "filmgenre", "filmclassification"]
    film = {}

    if result:
        for i, colname in enumerate(colnames):
            value = result[i]
            film[colname] = value
    return film


film_dao = FilmDAO()


def get_film_dao():
    return film_dao

# testing
def main():
    print('Get All:')
    films = film_dao.getAll()
    print(films)

    print('Get First Film:')
    print(film_dao.findByid(films[0]["id"]))

    print('Create new Film:')
    new_film = {}
    new_film["name"] = 'Batman Begins'
    new_film["director"] = 'Christopher Nolan'
    new_film["filmgenre"] = 'action adventure'
    new_film["filmclassification"] = 'pg'
    new_film["id"] = film_dao.create(new_film)

    # Make sure new film can be selected
    if new_film != film_dao.findByid(new_film["id"]):
        print('New film not created properly')
        return
    else:
        print(new_film)

    print('Update new Film:')
    new_film["filmgenre"] = 'superhero'
    film_dao.update(new_film)

    # Make film is updated
    if new_film != film_dao.findByid(new_film["id"]):
        print('New film did not update')
        return
    else:
        print(new_film)

    print('Delete new Film:')
    film_dao.delete(new_film["id"])

    if {} != film_dao.findByid(new_film["id"]):
        print('New film did not delete')
    else:
        print("Deleted:", new_film["id"])


if __name__ == '__main__':
    main()
