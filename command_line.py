import sys
import os
import argparse
from ProductionCode.utils import *

"""This file parses the command line arguments and provides instructions for what to do next."""
parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

parser.add_argument("--genres", nargs="+")
"""Usage statement for filter_by_genres: python3 commandline.py --genres [genres to filter by]"""
parser.add_argument("--title", type=str)
"""Usage statement for get_score: python3 commandline.py --title title"""

args = parser.parse_args()

if args.genres is not None:
    print(filter_by_genres(args.genres))
elif args.title is not None:
    get_score(args.title)
