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
    print(filter_by_genres(args.genres))
elif args.title is not None:
    get_score(args.title)


=======
    print(filter_by_genres(args.genres))
    
>>>>>>> e9dd4ff4f62f843d7c1404bad5ebd5e9828df6d7
