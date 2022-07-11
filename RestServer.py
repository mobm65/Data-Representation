from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path +'', statuc_folder = 'staticpages')


@app.route('/')
def index():
    return "hello"

# get all
@app.route('film')
def getAll():
    return jsonify([])

# find by id
@app.route('film/<int:id>')
def findById(id):
    return jsonify({})

create
curl--X-POST--d-"{\"name\":\"test\", \"director\":"guygal\", \"genre\":\"type"\, \"classification\":"val"}"
http://127.0.0.1:5000/film

@app.route('/film', methods=['POST'])
def create():
    #global nextId
    if not request.json:
        abort(400)
    
    film = {
        "id":request.json["id"],
        "name":request.json["name"],
        "director":request.json["director"],
        "genre":request.json["genre"],
        "classification":request.json["classification"]
    }
    return jsonify({})