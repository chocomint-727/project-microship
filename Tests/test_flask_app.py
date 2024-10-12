import unittest
from flask_app import *   

class testFlaskApp(unittest.TestCase):
    def test_one_genre(self):
        """Tests the genre function with one valid genre
        """
        self.app = app.test_client()
        response = self.app.get("/genres?genre=comedy").data
        self.assertEqual(b"[0,2,5,6,7]\n", response)
    
    def test_multiple_genre(self):
        """Tests the genre function with more than one valid genre
        """
        self.app = app.test_client()
        response = self.app.get("/genres?genre=comedy&genre=drama").data
        self.assertEqual(b"[0,2,6]\n", response)
 
    def test_no_genre(self):
        """Tests the genre function with no inputted genres
        """
        self.app = app.test_client()
        response = self.app.get("/genres").data
        self.assertEqual(b"[0,1,2,3,4,5,6,7,8,9]\n", response)
    
    def test_nonexistant_genre(self):
        """Tests the genre function with one invalid genre
        """
        self.app = app.test_client()
        response = self.app.get("/genres?genre=school").data
        self.assertEqual(b"[]\n", response)