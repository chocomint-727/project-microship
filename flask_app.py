from flask import Flask, request, render_template, abort
from ProductionCode.datasource import *
from ProductionCode.services import *

app = Flask(__name__)
sql = DataSource()
all_genres = ['Action', 'Adventure', 'Cars', 'Comedy', 'Dementia', 'Demons', 'Drama', 
             'Fantasy', 'Game', 'Historical', 'Horror', 'Josei', 'Kids', 'Magic', 
             'Martial Arts', 'Mecha', 'Military', 'Music', 'Mystery', 'Parody', 'Police', 
             'Psychological', 'Romance', 'Samurai', 'School', 'Sci-Fi', 'Seinen', 
             'Shoujo', 'Shoujo Ai', 'Shounen', 'Shounen Ai', 'Slice of Life', 'Space', 
             'Sports', 'Super Power', 'Supernatural', 'Thriller', 'Vampire', 'Yuri']
    
@app.route("/")
def home():
    ''' Renders the homepage. Not much else to say '''
    animes = sql.get_all_titles()
    return render_template("homepage.html", animes=animes, genres=all_genres)

@app.route("/search")
def search(): 
    ''' Interacts with the filter by genres function. 
        Because this function takes an arbitrary amount of arguments,
        get request parameters are used rather than a route 
        This function is abstracted into two component functions.
        '''
    query, genres, blacklist = extract_search_parameters()
    search_results = perform_search(query, genres, blacklist)
    return render_template("showlist.html", indices=search_results)

def extract_search_parameters():
    '''returns all of the parameters submitted in the form as individual lists'''
    query = request.args.getlist("title")[0]
    genres = [i.replace("_", " ") for i in request.args.getlist("genre")]
    blacklist = [i.replace("_", " ") for i in request.args.getlist("exclude")]
    return query, genres, blacklist

def perform_search(query, genres, blacklist):
    '''run the query on with the parameters extracted'''
    return sql.fuzzy_match_name(query, genres, blacklist)

@app.route("/title")
def title(): 
    ''' Interacts with the filter by genres function. 
        Employs a helper method to grab the thumbnail image on this page
        '''
    args = request.args.getlist("title")
    res=sql.get_data_from_title(args[0])
    blur = is_inappropriate_genre(res)
    if res == None:
        abort(404)
    else:
        img = get_image(res[3], res[4])
        return render_template("showpanel.html", info=res, imageLink=img, blur=blur) # return the indices in the list
    
@app.route("/rankings")
def rankings():
    ''' Renders the rankings page with the top-ranked anime based on their score '''
    default_limit = 25
    limit = request.args.get("limit", default_limit, type=int) 
    if limit <= 0:
        abort(404)
    top_animes = sql.get_top_ranked_anime(limit)
    if top_animes is None or len(top_animes) == 0:
        abort(404)
    else:
        return render_template("rankings.html", top_animes=top_animes, limit=limit)

@app.route("/random")
def random_anime():
    ''' Renders page for a random anime by calling get_random_anime and checking genres '''
    res = None
    while res is None or is_inappropriate_genre(res):
        res = sql.get_random_anime()[0] 

    img = get_image(res[3], res[4])  
    blur = is_inappropriate_genre(res)  
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

@app.route("/guide")
def guide():
    ''' Renders guide page '''
    return render_template("guide.html")

@app.errorhandler(404)
def page_not_found(e):
    ''' A helpful 404 error page is rendered when a 404 error is encountered.'''
    return render_template("error404.html")

@app.errorhandler(500)
def python_bug(e):
    ''' When a 500 error is encountered, a helpful 500 error page is rendered.'''
    return render_template("error500.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5210)
