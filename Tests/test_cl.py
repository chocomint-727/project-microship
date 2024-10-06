import subprocess
import unittest
import sys
import os
import csv

class TestClass(unittest.TestCase):

    """def setUp(self):
        load_data()"""

    def test_get_score_cowboy_bebop(self):
         expectedCode = subprocess.Popen(["python3", "ProductionCode/utils.py", "--title", "Cowboy Bebop"], 
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
         output, err = expectedCode.communicate()
         self.assertEqual(output.strip(), 8.78)
         expectedCode.terminate()



