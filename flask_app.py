from flask import Flask, request, render_template
import csv
from ProductionCode.datasource import *
from bs4 import BeautifulSoup
import requests

dset = []
app = Flask(__name__)
sql = DataSource()

def getImage(id, title):
    '''
    Scrapes the MAL page to grab the image using ID and title
    '''
    r = requests.get(f"https://myanimelist.net/anime/{id}")
    soup = BeautifulSoup(r.content, features="html.parser")
    img = list(soup.find_all(True, {"alt": title, "class": "ac"}))[0]["data-src"] 
    return img

@app.route("/")
def home():
    '''Render the homepage. Not much else to say'''
    return render_template("homepage.html")

@app.route("/title")
def title(): 
    args = request.args.getlist("title")
    ''' Interacts with the filter by genres function. 
        Employs a helper method to grab the thumbnail image on this page'''
    res=sql.get_data_from_title(args[0])
    print(res)
    img = getImage(res[0], res[1])
    return render_template("showpanel.html", info=res, imageLink=img) # return the indices in the list


@app.route("/random")
def randomAnime():
    res = sql.get_Random_Anime()[0]
    print(res)
    img = getImage(res[0], res[1])
    return render_template("showpanel.html", info=res, imageLink=img) # return the indices in the list

    

@app.route("/genres")
def filter(): 
    ''' Interacts with the filter by genres function. 
        Because this function takes an arbitrary amount of arguments,
        get request parameters are used rather than a route. '''
    query = request.args.getlist("genre") # get all args from the get request
    res=sql.filter_by_genres(query)
    return render_template("showlist.html", indices=res, ids = [f[0] for f in res]) # return the indices in the list

@app.errorhandler(404)
def page_not_found(e):
    return "Page not found. Remember that the URL convention is /title/(name of title) or /genres?genre=(genres to search by) <br> For example, /title/Trigun returns score and genre of an Anime with the title Trigun <br> /genres?genre=Action returns a table of Anime titles whose genre is action <br> /genres?genre=Action&genre=Comedy returns a table of Anime titles whose genre is action AND comedy!"

@app.errorhandler(500)
def python_bug(e):
    return "Uh oh! Something failed to run behind the scenes. For now you can return to the homepage, make sure the URL follows the guidelines, and contact the developers for help!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5211)
