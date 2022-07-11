# testing code 
from FilmDAO import FilmDAO

film1 = {
    "id":1,
    "name" : "Dr Who",
    "director":"Annetta Laufer",
    "genre":"science fiction",
    "classification":"g"
}

film2 = {
    "id":2,
    "name":"Daleks Invasion Earth",
    "director":"Gordon Flemyng",
    "genre":"science fiction",
    "classification": "pg"
}

returnValue = filmDAO.getall()
print(returnValue)
returnValue = filmDAO.findByid(film2["id"])
print(returnValue)
returnValue = filmDAO.update(film2)
print(returnValue)
returnValue = filmDAO.findByid(film2["id"])
print(returnValue)
returnValue = filmDAO.delete(film2["id"])
print(returnValue)