# CS257-F24-TeamTemplate
Template for long-term team projects for CS257 Software Design Fall 2024

NAMES:
- Christian Park
- Raaid Iqbal
- Omar Sobhy
- Matthew Hall

# Comments for the Flask Revision
The URL format for our functionality is as follows:

-Parentheses indicate that a particular part of the URL is variable. Do not actually enter parentheses in the URL.

-To enter get information for an anime based on the title, run the flask app and add /title?title=(name of title) to the website URL. This is not case sensitive.

-To filter the data by a genre, run the flask app and add /genres?genre=(genre to search by) to the website URL. This is not case sensitive. When on the page of anime from that genre, click on one of the rows to go to a page that displays the information about that anime in a more organized way.

-To filter the data by multiple genres, run the flask app and add /genres?genre=(genre to search by)&genre=(genre to search by) to the website URL adding as many ampersands as needed to search for as filter by as many genres as you want.

-To get information about a random anime, run the flask app and add /random to the website URL. This is case sensitive and "random" must be all lowercase.

# Comments for the Front-End Deliverable
Currently, the "Home," "Advanced Search," and "Rankings" buttons in the navigation bar do nothing. We will most likely implement these for the final version of the project and may add more buttons to the navigation bar. The two features that allow a user to get information from the database on our website are the non-case-sensitive autocomplete search bar on the homepage and the "Random" button in the navigation bar on the homepage. 
To use the search bar, you can type in the title of an anime in the database or start to type a title, and then select the full title from the dropdown of autocomplete options that appear, or you can type anything at all. Then, you press the purple button to the right of the search bar to display anime that contain the characters that you typed in. From here you can hover over the row for a particular anime and click on it to display a graphic that contains a promotional image of the anime and information such as the animation studio that produced it, its genres, and score.
To use the "Random" button in the navigation bar, click on it. This will display the same type of graphic from the search functionality, but for a random anime from our database. 
Additionally, anime of particular genres that we have reason to believe will produce NSFW promotional images via webscraping have their pictures blurred out in the graphic display of their information.


# Comments for the Database Deliverable
We kept all of the columns in the dataset because all of the information in these columns is displayed when users filter by genres in order to give them the most information possible about those anime. We also may make functions to filter by at least some of these other columns in the future.

# Command Line App Instructions
The command line app has two functionalities at the moment:
- Filtering by genres
    -  This function returns a list of the MAL IDs which match every genre inputted
- Accessing the rating of an anime by its title
    - This function gives a rating out of 10 as seen on MAL



To filter by genres, run <code>python3 command_line.py --genres [genres to filter by]</code><br>
For example, try <code>python3 command_line.py --genres action comedy</code><br>
This will output a list of all MAL IDs which match both action and comedy.



To access ratings, run <code>python3 command_line.py --title \[title\]</code><br>
For example, try <code>python3 command_line.py --title Trigun</code><br>
This will output the rating for Trigun, which is 8.24.

To run our tests, run python3 Tests/test_cl.py.
