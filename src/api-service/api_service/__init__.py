"""API-Service."""
__version__ = "0.1.0"

from flask import Flask
from flask_restful import Api

from api_service.resources.twentyfivestories import TwentyFiveStories
from api_service.resources.karmastories import KarmaStories
from api_service.resources.daysofposts import DaysOfPosts


def create_app():
    """Create instance of the FLASK application."""
    app = Flask(__name__)
    api = Api(app)

    # Register API
    api.add_resource(TwentyFiveStories, "/twenty_five_stories")
    api.add_resource(DaysOfPosts, "/days_of_posts")
    api.add_resource(KarmaStories, "/karma_stories")

    return app
