import sys
import os
import argparse
from ProductionCode.utils import *

parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

parser.add_argument("--genres", nargs="+")
parser.add_argument("--title", type=str)

args = parser.parse_args()

def filter_by_genres(genres):
    for g in genres:
        pass

if args.genres is not None:
    for r in filter_by_genres(args.genres):
        print(r, "\n")
elif args.title is not None:
    get_score(args.title)


