from flask import Flask, request
import csv
from ProductionCode.utils import *

dset = []
app = Flask(__name__)

def load_data():
    """ Loads data one row at a time from the dataset. """
    global dset
    with open("Data/command_line_testing_subset.csv", newline="") as f:
        reader = csv.reader(f)
        dset = [line for line in reader]
        
def format_html_table(indices):
    """ Implement an html table for displaying multiple rows at the same time """
    p = """<head>
            <title>Media Sorter</title>
            <style> table, td {
                border: 1px solid black;
                padding: 10px;
            }</style>
           </head>
           <body>
            <h1>Filtered TV Shows</h1><br>
           <table>"""
    
    for ix in indices:
        p += "<tr>"
        for data in dset[ix]:
            p += "<td>"
            p += data
            p += "</td>"
        p += "</tr>"
    
    p += "</table></body>"
    return p

@app.route("/genres")
def filter(): 
    """ interacts with the filter by genres function. 
        Because this function takes an arbitrary amount of arguments,
        get request parameters are used rather than a route. """   
    query = request.args.getlist("genre") # get all args from the get request
    return format_html_table(filter_by_genres(query)) # return the indices in the list

if __name__ == "__main__":
    load_data()
    app.run()