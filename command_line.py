import sys
import os
import argparse
from ProductionCode.datasource import *
sql = DataSource()


"""This file parses the command line arguments and provides instructions for what to do next."""
parser = argparse.ArgumentParser(
                    prog='Anime Browser',
                    description='Find the Anime of your dreams!',
                    epilog='With the Anime Browser tool, you can find all sorts of useful information on your current (or next!) favorite Anime. Get binging!')

parser.add_argument("--genres", nargs="+")
"""Usage statement for filter_by_genres: python3 command_line.py --genres [genres to filter by]"""
parser.add_argument("--title", type=str)
"""Usage statement for get_score: python3 command_line.py --title [some title]"""

args = parser.parse_args()

if args.genres is not None:
    print(sql.filter_by_genres(args.genres))
elif args.title is not None:
    print(sql.get_score_from_title(args.title))
