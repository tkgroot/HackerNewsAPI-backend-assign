"""API Service."""
from flask import Flask
from flask_restful import Resource, Api

from api_service.utilities.api_url import story_url_for
from api_service.resources.twentyfivestories import TwentyFiveStories
from api_service.resources.tenkkarmastories import KarmaStories

app = Flask(__name__)
api = Api(app)

# helpers


# Resources
class SevenDaysStories(Resource):
    """7 Days API Endpoint."""

    def get(self):
        """
        Get-Method.

        :return:
        """


# Register API
api.add_resource(TwentyFiveStories, "/twenty_five_stories")
api.add_resource(SevenDaysStories, "/seven_days_stories")
api.add_resource(KarmaStories, "/karma_stories")

if __name__ == "__main__":
    app.run(debug=True)
