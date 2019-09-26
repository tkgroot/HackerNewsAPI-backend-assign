"""API Service."""
import requests
from api_service.utilities.lang_processing import top_ten_words
from flask import Flask
from flask_restful import Resource, Api
from requests_futures.sessions import FuturesSession

from api_service.utilities.api_url import story_url_for, newstories_url, find_user_by
from api_service.resources.twentyfivestories import TwentyFiveStories

app = Flask(__name__)
api = Api(app)

# helpers
KARMA_LIMIT = 10000  # contains a constant for the karma limit


# Resources
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
        titles = ""
        new_stories_top500 = requests.get(url=newstories_url()).json()
        stories = new_stories_top500

        def res_hook(resp, *args, **kwargs):
            data = resp.json()
            username = data["by"] if data["by"] else None
            user = requests.get(url=find_user_by(username=username)).json()
            karma = user["karma"] if user["karma"] else 0

            if karma < KARMA_LIMIT:
                resp.data = {"title": ""}
            else:
                print("story_id", data["id"], "user_id", data["by"])
                resp.data = resp.json()["title"]

        session = FuturesSession()

        res_stories = [
            session.get(url=story_url_for(story_id), hooks={"response": res_hook})
            for story_id in stories
        ]

        for story in res_stories:
            story = story.result()
            titles += f" {story.data}"

        return top_ten_words(titles)


# Register API
api.add_resource(TwentyFiveStories, "/twenty_five_stories")
api.add_resource(SevenDaysStories, "/seven_days_stories")
api.add_resource(TenKKarmaStories, "/ten_k_karma_stories")

if __name__ == "__main__":
    app.run(debug=True)
