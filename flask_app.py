from flask import Flask, request, render_template, abort
from ProductionCode.datasource import *
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
sql = DataSource()
allgenres = ['Action', 'Adventure', 'Cars', 'Comedy', 'Dementia', 'Demons', 'Drama', 'Fantasy', 'Game', 'Historical', 'Horror', 'Josei', 'Kids', 'Magic', 'Martial Arts', 'Mecha', 'Military', 'Music', 'Mystery', 'Parody', 'Police', 'Psychological', 'Romance', 'Samurai', 'School', 'Sci-Fi', 'Seinen', 'Shoujo', 'Shoujo Ai', 'Shounen', 'Shounen Ai', 'Slice of Life', 'Space', 'Sports', 'Super Power', 'Supernatural', 'Thriller', 'Vampire', 'Yaoi', 'Yuri']

def getImage(id, title):
    ''' Scrapes the MAL page to grab the image using ID and title.
        If image is not found, returns a generic not found image
        '''
    try:
        r = requests.get(f"https://myanimelist.net/anime/{id}")
        soup = BeautifulSoup(r.content, features="html.parser")
        img = list(soup.find_all(True, {"alt": title, "class": "ac"}))[0]["data-src"] 
        return img
    except:
        img = "https://i.ibb.co/fHnD0Qx/notfound.png"
        return img

def blurImageCheck(res):
    ''' Checks if artwork should be blurred based on genre of anime 
        (some inappropriate genres) '''
    if res != None and ("Hentai" in res[6] or "Ecchi" in res[6] or "Harem" in res[6]):
        return True
    
@app.route("/")
def home():
    ''' Renders the homepage. Not much else to say '''
    animes = sql.get_all_titles()
    return render_template("homepage.html", animes=animes, genres=allgenres)

@app.route("/search")
def search(): 
    ''' Interacts with the filter by genres function. 
        Because this function takes an arbitrary amount of arguments,
        get request parameters are used rather than a route 
        '''
    query = request.args.getlist("title")[0] # get all args from the get request
    genres = request.args.getlist("genre")
    blacklist = request.args.getlist("exclude")
    res=sql.fuzzy_match_name(query, genres, blacklist)
    return render_template("showlist.html", indices=res, query=query, blacklist=blacklist, genres=genres, ids = [f[0] for f in res]) # return the indices in the list

@app.route("/title")
def title(): 
    ''' Interacts with the filter by genres function. 
        Employs a helper method to grab the thumbnail image on this page
        '''
    args = request.args.getlist("title")
    res=sql.get_data_from_title(args[0])
    blur = blurImageCheck(res)
    if res == None:
        abort(404)
    else:
        img = getImage(res[3], res[4])
        return render_template("showpanel.html", info=res, imageLink=img, blur=blur) # return the indices in the list
    
@app.route("/rankings")
def rankings():
    ''' Renders the rankings page with the top-ranked anime based on their score '''
    limit = request.args.get("limit", 25, type=int) 
    if limit <= 0:
        abort(404)
    top_animes = sql.get_top_ranked_anime(limit)
    if top_animes is None or len(top_animes) == 0:
        abort(404)
    else:
        return render_template("rankings.html", top_animes=top_animes, limit=limit)

@app.route("/random")
def randomAnime():
    ''' Renders page for a random anime by calling get_random_anime and checking genres '''
    
    res = None
    while res is None or blurImageCheck(res):
        res = sql.get_random_anime()[0] 

    img = getImage(res[3], res[4])  # Assuming res[3] and res[4] contain necessary data for the image
    blur = blurImageCheck(res)  # Check if the image should be blurred
    return render_template("showpanel.html", info=res, imageLink=img, blur=blur)

@app.route("/genres")
def filter(): 
    ''' Interacts with the filter by genres function. 
        Because this function takes an arbitrary amount of arguments,
        get request parameters are used rather than a route
        '''
    query = request.args.getlist("genre") # get all args from the get request
    res=sql.filter_by_genres(query)
    if query == [''] or res == []:
        abort(404)
    else: 
        return render_template("showlist.html", indices=res, ids = [f[3] for f in res]) # return the indices in the list

@app.route("/about")
def about():
    ''' Renders about page '''

    return render_template("about.html")

@app.errorhandler(404)
def page_not_found(e):
    ''' A helpful 404 error page is rendered when a 404 error is encountered.'''
    return render_template("error404.html")

@app.errorhandler(500)
def python_bug(e):
    ''' When a 500 error is encountered, a helpful 500 error page is rendered.'''
    return render_template("error500.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5242)
