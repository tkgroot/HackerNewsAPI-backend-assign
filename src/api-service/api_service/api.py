"""API Service."""
import requests
from flask import Flask
from flask_restful import Resource, Api
from requests_futures.sessions import FuturesSession

from api_service.utilities.api_url import newstories_url, story_url_for

app = Flask(__name__)
api = Api(app)

# helpers
MAX_STORIES = 25


# Resources
class TwentyFiveStories(Resource):
    """25 Stories API Endpoint."""
    def get(self):
        """
        GET-Method.

        requests the HackerNews API ``/newstories.json`` to retrieve the latest 500
        story ids, using 25 ids to request the story's content from HackerNews.
        The stories are then filtered the title extracted and merged together in one
        title string. This is is then passed into ``top_ten_words()`` to gather to top
        ten frequent used words.

        :return: {dict} - 10 frequent used words
        """
        titles = ""  # string representation of all titles
        # counts number of stories where the title can be extracted
        story_counter = 0

        new_stories_top500 = requests.get(url=newstories_url()).json()

        # reduce list to maximum stories required
        stories = new_stories_top500[:MAX_STORIES]

        # Query the 25th latest stories asynchronously by using their id from the
        # previous query.
        session = FuturesSession()

        res_stories = [session.get(story_url_for(idx=story_id)) for story_id in stories]
        for story in res_stories:
            content = story.result().json()

            # Validates the content to be existent and verify that the title key exists
            # Deleted stories are flagged with {deleted:True} and do not contain a
            # title key
            if content is not None and "title" in content:
                titles += f" {content['title']}"
                story_counter += 1

        return titles


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
