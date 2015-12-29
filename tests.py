#!venv/bin/python3
import os
import unittest

from config import basedir
from app import app, db
from app.models import Post, Comment

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['MONGODB_SETTINGS'] = {'DB': 'test'}
        self.app = app.test_client()


    def test_unique_slug(self):
        
