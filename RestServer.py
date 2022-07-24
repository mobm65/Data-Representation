from FilmDAO import get_film_dao
from flask import Flask, url_for, request, redirect, abort, jsonify
app = Flask(__name__)
film_dao = get_film_dao()

@app.route('/')
def index():
    return "hello"

# get all
@app.route('/film')
def getAll():
    return jsonify(film_dao.getAll())

# find by id
@app.route('/film/<int:id>')
def findById(id):
    return jsonify(film_dao.findByid(id))

# create
# curl--X-POST--d-"{\"name\":\"test\", \"director\":\"guygal\", \"genre\":\"type\", \"classification\":\"val\}"
# -http://127.0.0.1:5000/film

#@app.route('/film', methods=['POST'])
#def create():
#    #global nextId
#    if not request.json:
#        abort(400)
#    
#    film = {
#        "id":request.json["id"],
#        "name":request.json["name"],
#        "director":request.json["director"],
#        "genre":request.json["genre"],
#        "classification":request.json["classification"]
#    }
#    return jsonify({})

if __name__ == '__main__':
    app.run()
