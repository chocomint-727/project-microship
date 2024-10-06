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
print(args.genres)
print(args.title)

if args.genres is not None:
    for r in filter_by_genres(args.genres):
        print(r, "\n")
    