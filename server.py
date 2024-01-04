# Dapa representation course 2023/24
# This file (server.py) is to create an application server for the API designed for
# Data representation 2023/24 project Type A.


# By: Eva Czeyda-Pommersheim
# Importing packages:
from flask import Flask, url_for, request, redirect, abort, jsonify
from movieDAO import movieDAO

app = Flask(__name__, static_url_path='', static_folder = '.')

# myMovies = [
   # {"id": 1, "Category": "Drama", "Title": "The Shawshank Redemption", "Director": "Frank Darabont", "Actor": "Morgan Freeman", "Year" : 1994},
   # {"id": 2, "Category": "Drama, Mystery, Thriller", "Title": "The Sixth Sense", "Director": "M. Night Shyamalan", "Actor": "Bruce Willis", "Year" : 1999},
   # {"id": 3, "Category": "Drama, Romance", "Title": "Forrest Gump", "Director": "Robert Zemeckis", "Actor": "Tom Hanks", "Year" : 1994},
   # {"id": 4, "Category": "Drama, Romance, Comedy", "Title": "The Terminal", "Director": "Steven Spielberg", "Actor": "Tom Hanks", "Year" : 2004},
   # {"id": 5, "Category": "Drama, Romance, Comedy", "Title": "As Good as it gets", "Director": "James L. Brooks", "Actor": "Jack Nicholson", "Year" : 1997},
   # {"id": 6, "Category": "Drama, Romance, Comedy", "Title": "The Terminal", "Director": "Steven Spielberg", "Actor": "Tom Hanks", "Year" : 2004},
#]
# nextId = 7
@app.route('/')
def index():
    return "Welcome to a list of some of my favourite movies!"

# Get all movies
# curl http://127.0.0.1:5000/myMovies
@app.route('/myMovies')
def getAll():
    results = movieDAO.getAll()
    return jsonify(results)
  

#find by ID
# curl http://127.0.0.1:5000/myMovies/1
@app.route('/myMovies/<int:id>')
def findById(id):
    #found = list(filter(lambda t : t["id"]== id, myMovies))
    #if len(found) == 0:
       # return jsonify(()) , 204
    #return jsonify(found[0])
    foundId = movieDAO.findByID(id)
    return jsonify(foundId)

# Find by year
# curl http://127.0.0.1:5000/myMovies/1992
@app.route('/myMovies/<int:Year>')
def findByYear(year):
    #found = list(filter(lambda t : t["Year"]== year, myMovies))
    #if len(found) == 0:
    #    return jsonify(()) , 204
    #return jsonify(found)
    foundYear = movieDAO.findByYear(year)
    return jsonify(foundYear)

# create
#curl -X "POST" -H "content-type:application/json" -d "{\"Category\": \"Romance, Comedy\",\"Title\":\"The Holiday\", \"Director\":\"Nancy Meyers\", \"Actor\":\"Cameron Diaz, Kate Winslet\", \"Year\":2006}" http://127.0.0.1:5000/myMovies

@app.route('/myMovies', methods = ['POST'])
def create():
    
    if not request.json:
        abort(400)

    movie = {
        
        "Category": request.json["Category"],
        "Title": request.json["Title"],
        "Director": request.json["Director"],
        "Actor": request.json["Actor"],
        "Year" : request.json["Year"]
    }
    values = (movie['Category'], movie['Title'], movie['Director'], movie['Actor'], movie['Year'])
    newId = movieDAO.create(values)
    movie['id'] = newId
    return jsonify(movie)
    #myMovies.append(movie)
    #nextId+= 1
    #return jsonify(movie)

# update
# curl -X "PUT" -H "content-type:application/json" -d "{\"Actor\":\"Cameron Diaz, Kate Winslet, Jude Law, Jack Black\",}" http://127.0.0.1:5000/myMovies/7
@app.route('/myMovies/<int:id>', methods = ['PUT'])
def update(id):
    #found = list(filter(lambda t : t["id"]== id, myMovies))
    #if len(found) == 0:
    #    return jsonify(()) , 404
    #currentMovie = found[0]
    
    #if 'Category' in request.json:
    #    currentMovie['Category'] = request.json['Category']
    #if 'Title' in request.json:
    #    currentMovie['Title'] = request.json['Title']
    #if 'Director' in request.json:
    #    currentMovie['Director'] = request.json['Director']
    #if 'Actor' in request.json:
    #    currentMovie['Actor'] = request.json['Actor']
    #if 'Price' in request.json:
    #    currentMovie['Year'] = request.json['Year']
    #return jsonify(currentMovie)
    foundMovie = movieDAO.findByID(id)
    if not foundMovie:
        abort(404)
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Year' in reqJson and type(reqJson['Year']) is not int:
        abort(400)
    
    if 'Category' in reqJson:
        foundMovie['Category'] = reqJson['Category']
    if 'Title' in reqJson:
        foundMovie['Title'] = reqJson['Title']
    if 'Director' in reqJson:
        foundMovie['Director'] = reqJson['Director']
    if 'Actor' in reqJson:
        foundMovie['Actor'] = reqJson['Actor']
    if 'Year' in reqJson:
        foundMovie['Year'] = reqJson['Year']
    values = (foundMovie['Category'], foundMovie['Title'], foundMovie['Director'], foundMovie['Actor'], foundMovie['Year'])
    movieDAO.update(values)
    return jsonify(foundMovie)


#delete
# curl -X "DELETE" http://127.0.0.1:5000/myMovies/7
@app.route('/myMovies/<int:id>', methods = ['DELETE'])
def delete(id):
    #found = list(filter(lambda t : t["id"]== id, myMovies))
    #if len(found) == 0:
    #    return jsonify(()) , 404
    
    #myMovies.remove(found[0])

    #return jsonify({"done" : True})
    movieDAO.delete(id)
    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)