import os
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from config import basedir, ADMINS

app = Flask(__name__)
app.config.from_object('config')

db = MongoEngine(app)

def register_blueprints(app):
    from app.views import posts
    from app.admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)


register_blueprints(app)
