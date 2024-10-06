import sys
import os
import argparse

parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

parser.add_argument("--genres", nargs="+")
parser.add_argument("--title", type=str)

args = parser.parse_args()
print(args.genres)
print(args.title)

def filter_by_genres(genres):
    for g in genres:
        pass