import unittest
from app.models import Article, Source

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("CNN", "Samuel", "test_title", "test_description", "simpleurl.com", "image_url", "02-05-2022", "article_content")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))



class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("123", "CNN", "cnn.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))