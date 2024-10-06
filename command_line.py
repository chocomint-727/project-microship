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

if args.genres is not None:
    print(filter_by_genres(args.genres))
elif args.title is not None:
    get_score(args.title)
