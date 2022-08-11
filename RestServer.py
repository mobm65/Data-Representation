# Creating the server
from FilmDAO import get_film_dao
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
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

# delete by id


@app.route('/film/<int:id>', methods=['DELETE'])
def delete(id):
    return film_dao.delete(id)

# add new film


@app.route('/film', methods=['POST'])
def create():
    if not request.json:
        abort(400)

    film = {
        "name": request.json["name"],
        "director": request.json["director"],
        "filmgenre": request.json["filmgenre"],
        "filmclassification": request.json["filmclassification"]
    }

    response = {}
    response['id'] = film_dao.create(film)
    return response


if __name__ == '__main__':
    app.run()
