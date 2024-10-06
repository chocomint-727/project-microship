import subprocess
import unittest
import sys
import os
import csv

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adaptable parent directory so we can import the utils file. solution that works on any os thanks to not hardcoding a path

# Add the parent directory to the system path
sys.path.append(parent_dir)

sys.path.append(parent_dir)
from ProductionCode.utils import *

class TestClass(unittest.TestCase):

    """def setUp(self):
        load_data()"""

    def test_get_score_cowboy_bebop(self):
         expectedCode = subprocess.Popen(["python3", "command_line.py", "--title", "Cowboy Bebop"], 
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
         output, err = expectedCode.communicate()
         self.assertEqual(output.strip(), "8.78")
         expectedCode.terminate()


    def test_get_score_incorrect_title(self):
         """This tests the edge case for get_score when an invalid title is inputted. An empty string should be retired."""
         expectedCode = subprocess.Popen(["python3", "ProductionCode/utils.py", "--title", "Space Jam"], 
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
         output, err = expectedCode.communicate()
         self.assertEqual(output.strip(), "")
         expectedCode.terminate()
    
    

unittest.main()
