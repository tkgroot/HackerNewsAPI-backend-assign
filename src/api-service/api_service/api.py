"""API Service."""
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# Resources
class TwentyFiveStories(Resource):
    """25 Stories API Endpoint."""
    def get(self):
        """
        Get-Method.
        :return:
        """
        return True


class SevenDaysStories(Resource):
    """7 Days API Endpoint."""
    def get(self):
        """
        Get-Method.
        :return:
        """
        return True


class TenKKarmaStories(Resource):
    """Users 10.000 Karma Points Story API Endpoint."""
    def get(self):
        """
        GET-Method.
        :return:
        """
        return True


# Register API
api.add_resource(TwentyFiveStories, "/twenty_five_stories")
api.add_resource(SevenDaysStories, "/seven_days_stories")
api.add_resource(TenKKarmaStories, "/ten_k_karma_stories")

if __name__ == "__main__":
    app.run(debug=True)
