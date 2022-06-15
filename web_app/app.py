import re
from recommender import recommend_5
from flask import Flask, render_template, request
from utils import movie_dict, top10_dict

# construct our flask instance, pass name of module
app = Flask(__name__)

# route decorator for mapping urls to functions
@app.route('/')
def welcome():
    return render_template('index.html',name="Sriracha's 🌶 Movie Recomendor",movies=list(movie_dict.values()))

@app.route('/topten')
def topten():
    """
    returns a list of top 10 recomended movies
    """
    movies = list(top10_dict.keys())
    return  render_template('topten.html',movies=movies)

@app.route('/recommend')
def recommend():
    """
    renders user ratings from url
    calls on NMF recomender function
    returns a list of 5 user_specific recomended movies
    """

    print(request.args)
    titles = request.args.getlist('title')
    ratings = request.args.getlist('rating')
    print(titles,ratings)
    user_rating = dict(zip(titles,ratings)) 
    movie_names = recommend_5(user_rating)
    return  render_template('recommender.html',movie_names=movie_names)

# main module
if __name__=='__main__':
    app.run(debug=True,port=5000)
