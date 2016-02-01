from flask import Flask
from flask.ext.mongoengine import MongoEngine

db = MongoEngine()


def create_app(**config_overrides):
    app = Flask(__name__)
    app.config.from_object('config')
    app.config.update(config_overrides)

    db.init_app(app)
    register_blueprints(app)

    return app


def register_blueprints(app):
    from blog.views import posts
    from blog.admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)


