import sys 
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adaptable parent directory so we can import the utils file. solution that works on any os thanks to not hardcoding a path
sys.path.append(parent_dir) # adding the parent directory to the system path

import unittest
from flask_app import *   

class TestHomepage(unittest.TestCase):
    def test_route(self):
        ''' Tests the standard case for the homepage and this is also an integration test that makes sure
        that flask is working.'''
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'Welcome to the homepage! Type in', response.data)

    def test_route_no_title(self):
        ''' Tests the edge case of user not writing a title at all '''
        self.app = app.test_client()
        response = self.app.get('/title/', follow_redirects=True)
        self.assertIn(b'Page not found', response.data)

    def test_valid_title(self):
        ''' Tests for a valid title - should include the same title as the input one '''
        self.app = app.test_client()
        response = self.app.get('/title/Trigun', follow_redirects=True)
        self.assertIn(b'Trigun', response.data)

    def test_invalid_capitalization_title(self):
        ''' Tests the edge case of a valid title typed with incorrect capitlization - 
        should include None for score, as get_score returns None '''
        self.app = app.test_client()
        response = self.app.get('/title/trigun', follow_redirects=True)
        self.assertIn(b'not found in the dataset', response.data)

    def test_valid_score(self):
        ''' Tests for a valid title that is one word - should include a valid score '''
        self.app = app.test_client()
        response = self.app.get('/title/Trigun', follow_redirects=True)
        self.assertIn(b'Score: 8.24', response.data)
        
    def test_valid_multiple_word_title(self):
        """This tests get_Score for a valid title that is multiple words."""
        self.app = app.test_client()
        response = self.app.get('/title/Cowboy Bebop', follow_redirects=True)
        self.assertIn(b'Score: 8.78', response.data)

    def test_valid_genre(self):
        ''' Tests the get_genre function with a valid one word title  '''
        self.app = app.test_client()
        response = self.app.get('/title/Monster', follow_redirects=True)
        self.assertIn(b'Drama, Horror, Mystery, Police, Psychological, Seinen, Thriller', response.data)

    def test_valid_genre_multiple_words(self):
        """This tests get_genre for a valid title that is multiple words."""
        self.app = app.test_client()
        response = self.app.get('/title/Cowboy Bebop', follow_redirects=True)
        self.assertIn(b'Action, Adventure, Comedy, Drama, Sci-Fi, Space', response.data)

    def test_one_genre(self):
        """Tests the filter_by_genre function with one valid genre
        """
        self.app = app.test_client()
        response = self.app.get("/genres?genre=comedy").data
        self.assertIn(b"[1, 4, 5, 6]", response)
    
    def test_multiple_genre(self):
        """Tests the filter_by_genre function with more than one valid genre
        """
        self.app = app.test_client()
        response = self.app.get("/genres?genre=comedy&genre=drama").data
        self.assertIn(b"[1, 5]", response)
 
    def test_no_genre(self):
        """Tests the filter_by_genre function with no inputted genres
        """
        self.app = app.test_client()
        response = self.app.get("/genres").data
        self.assertIn(b"[0, 1, 2, 3, 4, 5, 6, 7, 8]", response)
    
    def test_nonexistant_genre(self):
        """Tests the filter_by_genre function with one invalid genre
        """
        self.app = app.test_client()
        response = self.app.get("/genres?genre=school").data
        self.assertIn(b"[]", response)
        
if __name__ == "__main__":  
    unittest.main()