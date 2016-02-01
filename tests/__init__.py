import blog
import unittest


class BaseTestCase(unittest.TestCase):
    """Parent class of all test cases"""

    def setUp(self):
        self.db_name = 'project_m_test'
        self.app = blog.create_app(MONGODB_SETTINGS={'DB': self.db_name,
                                                     'HOST': 'masunghoon.asuscomm.com'},
                                   TESTING=True)
        self.ctx = self.app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()
