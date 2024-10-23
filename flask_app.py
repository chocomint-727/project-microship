from flask import Flask, request
import csv
from ProductionCode.datasource import *

dset = []
app = Flask(__name__)
sql = DataSource()

def get_title_info(title):
    ''' Helper function that gets title info from input title, returns score and genre '''
    score = sql.get_score_from_title(title) 
    genre = sql.get_genre_from_title(title)
    return score, genre


def format_html_table(indices):    
    
    ids = [f[0] for f in indices]    
    
    """ Implement an html table for displaying multiple rows at the same time """
    p = """<head>
            <title>Media Sorter</title>
            <style> td {
                cursor: pointer;
                border: 1px solid black;
                border-radius: 15px;
                border-spacing: 10px;
                padding: 10px;
                background-color: white;
                text-align: center;
            }
            td:hover {
                background-color: coral;
            }</style>
            <!""" + str(ids) + """>
           </head>
           <body>
            <h1>Filtered TV Shows</h1><br>
           <table>"""
    
    for ix in indices:
        p += "<tr>"
        for data in ix:
            p += "<td>"
            p += str(data)
            p += "</td>"
        p += "</tr>"
    
    p += "</table></body>"
    return p

@app.route('/')
def homepage():
    ''' Returns what is to be displayed on the homepage '''
    titles = "Cowboy Bebop, Cowboy Bebop: Tengoku no Tobira, Trigun, Witch Hunter Robin, Bouken Ou Beet, Eyeshield 21, Hachimitsu to Clover, Hungry Heart: Wild Striker, Initial D Fourth Stage, Monster"
    display = "Welcome to the homepage! Type in '/title/(title)/' where (title) is the name of the show to get information about an anime. brackets! <br> It currently only displays title and score. <br><br> Titles you can try: <br> " + titles
    display += "<br><br>To search for shows by their genres, use /genres! Make sure to include get request arguments with the genres you want to include."
    return display

@app.route('/title/<title>/', strict_slashes = False)
def display_title_info(title):
    ''' Displays title info. If title does not exist, say it is not found in dataset '''
    score, genre = get_title_info(title)
    if score is None or genre is None:
        return f"Title '{title}' not found in the dataset."
    display = f"Title:  {title} <br> Score: {str(score)} <br> Genre: {genre}"
    return display

@app.route("/genres")
def filter(): 
    """ Interacts with the filter by genres function. 
        Because this function takes an arbitrary amount of arguments,
        get request parameters are used rather than a route. """   
    query = request.args.getlist("genre") # get all args from the get request
    return format_html_table(sql.filter_by_genres(query)) # return the indices in the list

@app.errorhandler(404)
def page_not_found(e):
    return "Page not found. Remember that the URL convention is /title/(name of title) or /genres?genre=genre_to_search_by!"

@app.errorhandler(500)
def python_bug(e):
    return "Uh oh! Something failed to run behind the scenes. For now you can return to the homepage, make sure the URL follows the guidelines, and contact the developers for help!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5135)
