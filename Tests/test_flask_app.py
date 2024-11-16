
import sys 
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adaptable parent directory so we can import the utils file. solution that works on any os thanks to not hardcoding a path
sys.path.append(parent_dir) # adding the parent directory to the system path

import unittest
from flask_app import *   
from ProductionCode.datasource import *
sql = DataSource()

class TestHomepage(unittest.TestCase):
    def test_route(self):
        ''' Tests the standard case for the homepage and this is also an integration test that makes sure
        that flask is working.'''
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'Next Episode', response.data)     

    def test_route_no_title(self):
        ''' Tests the edge case of user not writing a title at all '''
        self.app = app.test_client()
        response = self.app.get('/title?title=', follow_redirects=True)
        self.assertIn(b'Page not found', response.data)

    def test_valid_title(self):
        ''' Tests for a valid title - should include the same title as the input one '''
        self.app = app.test_client()
        response = self.app.get('/title?title=Trigun', follow_redirects=True)
        self.assertIn(b'Trigun', response.data)

    def test_invalid_capitalization_title(self):
        ''' Tests the edge case of a valid title typed with incorrect capitlization - 
        should show normal page for title as capitalization is automatically handled
        '''
        self.app = app.test_client()
        response = self.app.get('/title?title=trigun', follow_redirects=True)
        self.assertIn(b'Trigun', response.data)

    def test_valid_score(self):
        ''' Tests for a valid title that is one word - should include a valid score '''
        self.app = app.test_client()
        response = self.app.get('/title?title=Trigun', follow_redirects=True)
        self.assertIn(b'Score', response.data)
        self.assertIn(b'<td class="data">8.24</td>', response.data)

    def test_valid_multiple_word_title(self):
        ''' This tests  for a valid title that is multiple words.'''
        self.app = app.test_client()
        response = self.app.get('/title?title=Cowboy Bebop', follow_redirects=True)
        self.assertIn(b'Score', response.data)
        self.assertIn(b'<td class="data">8.78</td>', response.data)

    def test_valid_genre(self):
        ''' Tests the get_genre function with a valid one word title  '''
        self.app = app.test_client()
        response = self.app.get('/title?title=Monster', follow_redirects=True)
        self.assertIn(b'Drama, Horror, Mystery, Police, Psychological, Seinen, Thriller', response.data)

    def test_valid_genre_multiple_words(self):
        ''' This tests get_genre for a valid title that is multiple words.'''
        self.app = app.test_client()
        response = self.app.get('/title?title=Cowboy Bebop', follow_redirects=True)
        self.assertIn(b'Action, Adventure, Comedy, Drama, Sci-Fi, Space', response.data)

    def test_one_genre(self):
        ''' Tests the filter_by_genre function with one valid genre
        '''
        self.app = app.test_client()
        response = self.app.get("/genres?genre=comedy").data
        self.assertIn(b"1, 6, 15, 16, 17", response)
    
    def test_multiple_genre(self):
        ''' Tests the filter_by_genre function with more than one valid genre
        '''
        self.app = app.test_client()
        response = self.app.get("/genres?genre=comedy&genre=drama").data
        self.assertIn(b"1, 6, 16", response)
 
    def test_no_genre(self):
        ''' Tests the filter_by_genre function with no inputted genres
        '''
        self.app = app.test_client()
        response = self.app.get("/genres").data
        self.assertIn(b"1, 5, 6, 7, 8, 15, 16, 17, 18, 19", response)
    
    def test_nonexistant_genre(self):
        ''' Tests the filter_by_genre function with one invalid genre
        '''
        self.app = app.test_client()
        response = self.app.get("/genres?genre=schools").data
        self.assertIn(b"Page not found", response)
        
    def test_valid_and_invalid_genre(self):
        ''' Tests the filter_by_genre function with a valid genre and an invalid genre, which should
        return a 404 error.'''
        self.app = app.test_client()
        response = self.app.get("/genres?genres=Seinen&genre=nonsense").data
        self.assertIn(b"Page not found", response)    

if __name__ == "__main__":  
    unittest.main()