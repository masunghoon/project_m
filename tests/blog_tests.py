import unittest
import blog
import mongoengine
from tests import BaseTestCase


class BlogTestCase(BaseTestCase):
    def setUp(self):
        super(BlogTestCase, self).setUp()

    def tearDown(self):
        blog.db.connection.drop_database(self.db_name)

    def test_create_app(self):
        assert self.app.config['TESTING']
        assert mongoengine.connection.get_db().name == 'project_m_test'
        rv = self.app.test_client().get('/')
        print(rv.data)
        assert b'No entries here so far' in rv.data


if __name__ == '__main__':
    unittest.main()
