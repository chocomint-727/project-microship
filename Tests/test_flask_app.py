import unittest
from flask_app import *   

class TestHomepage(unittest.TestCase):
    def test_route(self):
        ''' Tests the standard case for the homepage '''
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'Welcome to the homepage! Type in', response.data)

class TestMissingTitleInURL(unittest.TestCase):
    def test_route(self):
        ''' Tests the edge case of user not writing a title at all '''
        self.app = app.test_client()
        response = self.app.get('/title/', follow_redirects=True)
        self.assertIn(b'Page not found', response.data)

class TestAnime(unittest.TestCase):
    def test_valid_title(self):
        ''' Tests for a valid title - should include the same title as the input one '''
        self.app = app.test_client()
        response = self.app.get('/title/Trigun', follow_redirects=True)
        self.assertIn(b'Trigun', response.data)

    def test_invalid_title(self):
        ''' Tests the edge case of an invalid title - should include None for score, as get_score returns None '''
        self.app = app.test_client()
        response = self.app.get('/title/trigun', follow_redirects=True)
        self.assertIn(b'not found in the dataset', response.data)

    def test_valid_score(self):
        ''' Tests for a valid title - should include a valid score '''
        self.app = app.test_client()
        response = self.app.get('/title/Trigun', follow_redirects=True)
        self.assertIn(b'Score: 8.24', response.data)

    def test_valid_genre(self):
        ''' Tests for a valid title - should include a valid score '''
        self.app = app.test_client()
        response = self.app.get('/title/Monster', follow_redirects=True)
        self.assertIn(b'Drama, Horror, Mystery, Police, Psychological, Seinen, Thriller', response.data)
        
class TestGetCell(unittest.TestCase):
    def test_invalid_index_access(self):
        ''' Tests the standard case  of entering valid cold/row indices for cell '''
        self.app = app.test_client()
        response = self.app.get('/1/1', follow_redirects=True)
        self.assertIn(b'Cowboy Bebop', response.data)

    def test_invalid_index_access(self):
        ''' Tests the edge case of entering invalid col/row indices (nonexistent cell in dataset) '''
        self.app = app.test_client()
        response = self.app.get('/9999/999', follow_redirects=True)
        self.assertIn(b'Cell not found', response.data)

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