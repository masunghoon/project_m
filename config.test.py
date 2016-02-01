import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'project_m-secret-key-is-public'

basedir = os.path.abspath(os.path.dirname(__file__))

MONGODB_DB = 'project_m_test'
MONGODB_HOST = 'masunghoon.asuscomm.com'
TESTING = True

# administrator list
ADMINS = ['masunghoon@gmail.com']
