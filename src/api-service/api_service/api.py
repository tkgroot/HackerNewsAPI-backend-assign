"""API Service."""
from flask import Flask
from flask_restful import Api

from api_service.resources.twentyfivestories import TwentyFiveStories
from api_service.resources.daysofposts import DaysOfPosts
from api_service.resources.tenkkarmastories import KarmaStories

app = Flask(__name__)
api = Api(app)


# Register API
api.add_resource(TwentyFiveStories, "/twenty_five_stories")
api.add_resource(DaysOfPosts, "/days_of_posts")
api.add_resource(KarmaStories, "/karma_stories")

if __name__ == "__main__":
    app.run(debug=True)
