import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'project_m-secret-key-is-public'

basedir = os.path.abspath(os.path.dirname(__file__))

MONGODB_SETTINGS = {'DB': 'project_m'}

# administrator list
ADMINS = ['masunghoon@gmail.com']
