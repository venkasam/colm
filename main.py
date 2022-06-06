from flask import Flask, jsonify, request
import csv
from demo import output
from age import get

allmovies=[]
likemovie2=[]
notlikemovie=[]
didnot=[]
with open("movie.csv",encoding="utf8")as f:
    reader=csv.reader(f)
    data=list(reader)
    allmovies=data[1:]
app=Flask(__name__)
@app.route("/get-movie")
def getmovie():
    movie_data={
        "title": allmovies[0][19], 
        "poster_link": allmovies[0][27],
        "release_date": allmovies[0][13] or "N/A", 
        "duration": allmovies[0][15],
        "rating": allmovies[0][20], 
        "overview": allmovies[0][9]
        }
    return jsonify({
        "data":allmovies[0],
        "status":"success"
        
    })
@app.route("/liked-movie", methods=["POST"]) 
def liked_movie(): 
    movie = allmovies[0] 
    likemovie2.append(movie) 
    allmovies.pop("0")
    return jsonify({ "status": "success" }), 201 
@app.route("/unliked-movie", methods=["POST"]) 
def unliked_movie(): 
    movie = allmovies[0] 
    
    notlikemovie.append(movie)
    allmovies.pop("0") 
    return jsonify({ "status": "success" }), 201 

@app.route("/did-not-watch", methods=["POST"]) 
def did_not_watch():
    movie = allmovies[0] 
    
    didnot.append(movie) 
    allmovies.pop("0") 
    return jsonify({ "status": "success" }), 201
@app.route("/popular-movies") 
def popular_movies(): 
    movie_data = [] 
    for movie in output: 
        _d = { "title": movie[0], "poster_link": movie[1], "release_date": movie[2] or "N/A", "duration": movie[3], "rating": movie[4], "overview": movie[5] } 
        movie_data.append(_d) 
    return jsonify({ "data": movie_data, "status": "success" }), 200
@app.route("/recommended-movies") 
def recommended_movies(): 
    all_recommended = [] 
    for liked_movie in likemovie2: 
      output = get(liked_movie[19]) 
    for data in output: all_recommended.append(data) 
    import itertools 
    all_recommended.sort() 
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended)) 
    movie_data = [] 
    for recommended in all_recommended: 
          _d = { "title": recommended[0], "poster_link": recommended[1], "release_date": recommended[2] or "N/A", "duration": recommended[3], "rating": recommended[4], "overview": recommended[5] } 
          movie_data.append(_d) 
    return jsonify({ "data": movie_data, "status": "success" }), 200
if __name__ =="__main__":
    app.run()

