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
         """This tests whether get_score correctly returns the score when an anime that is in the dataset is inputted."""
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
         
    def test_get_score_cowboy_bebop_lowercase(self):
            """This tests the edge case where a correct anime title is input into get_score, but the capitalization is incorrect."""
            expectedCode = subprocess.Popen(["python3", "ProductionCode/utils.py", "--title", "cowboy bebop"], 
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
            output, err = expectedCode.communicate()
            self.assertEqual(output.strip(), "")
            expectedCode.terminate()

    def test_test_filter_by_one_genre_valid(self):
         expectedCode = subprocess.Popen(["python3", "command_line.py", "--genres", "Action"],
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
         output, err = expectedCode.communicate()
         self.assertEqual(output.strip(), '[1, 5, 6, 7, 15, 18]')
         expectedCode.terminate()


    def test_filter_by_genre_invalid_genre(self):
         expectedCode = subprocess.Popen(["python3", "command_line.py", "--genres", "FakeGenre"],
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
         output, err = expectedCode.communicate()
         self.assertEqual(output.strip(), '[]')
         expectedCode.terminate()


    def test_filter_by_genre_invalid_partial(self):
         expectedCode = subprocess.Popen(["python3", "command_line.py", "--genres", "Action", "FakeGenre"],
                                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
         output, err = expectedCode.communicate()
         self.assertEqual(output.strip(), '[]')
         expectedCode.terminate()
    
    def test_filter_by_genre_no_comibination(self):
         expectedCode = subprocess.Popen(["python3", "command_line.py", "--genres", "Supernatural", "Comedy"],
                                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
         output, err = expectedCode.communicate()
         self.assertEqual(output.strip(), '[]')
         expectedCode.terminate()
         
         
    def test_filter_by_genre_many_genres(self):
         expectedCode = subprocess.Popen(["python3", "command_line.py", "--genres", "Drama", "Horror", "Mystery", "Police", "Psychological", "Seinen", "Thriller"],
                                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
         output, err = expectedCode.communicate()
         self.assertEqual(output.strip(), '[19]')
         expectedCode.terminate()
         
    def test_filter_by_genre_no_input(self):
         expectedCode = subprocess.Popen(["python3", "command_line.py", "--genres", ""],
                                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
         output, err = expectedCode.communicate()
         self.assertEqual(output.strip(), '')
         expectedCode.terminate()
         
    def test_filter_by_genre_no_comibination(self):
         expectedCode = subprocess.Popen(["python3", "command_line.py", "--genres", "Supernatural", "Comedy"],
                                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
         output, err = expectedCode.communicate()
         self.assertEqual(output.strip(), '[]')
         expectedCode.terminate()
         
    def test_filter_by_genre_case_sensitive(self):
         expectedCode = subprocess.Popen(["python3", "command_line.py", "--genres", "AcTIon"],
                                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
         output, err = expectedCode.communicate()
         self.assertEqual(output.strip(), '[1, 5, 6, 7, 15, 18]')
         expectedCode.terminate()



    

unittest.main()