# CS257-F24-TeamTemplate
Template for long-term team projects for CS257 Software Design Fall 2024

NAMES:
- Christian Park
- Raaid Iqbal
- Omar Sobhy
- Matthew Hall

# Command Line App Instructions
The command line app has two functionalities at the moment:
- Filtering by genres
    -  This function returns a list of the MAL IDs which match every genre inputted
- Accessing the rating of a show by its title
    - This function gives a rating out of 10 as seen on MAL



To filter by genres, run <code>python3 command_line.py --genres [genres to filter by]</code><br>
For example, try <code>python3 command_line.py --genres action comedy</code><br>
This will output a list of all MAL IDs which match both action and comedy.



To access ratings, run <code>python3 command_line.py --title \[title\]</code><br>
For example, try <code>python3 command_line.py --title Trigun</code><br>
This will output the rating for Trigun, which is 8.24.
