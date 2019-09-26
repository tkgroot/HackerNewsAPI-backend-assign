"""Resource for API Service."""
import requests
from flask_restful import Resource
from requests_futures.sessions import FuturesSession

from api_service.utilities.api_url import newstories_url, find_user_by, story_url_for
from api_service.utilities.lang_processing import top_ten_words

KARMA_LIMIT = 10000  # contains a constant for the karma limit


def res_hook(resp, *args, **kwargs):
    """Response hook."""
    data = resp.json()
    username = data["by"] if data["by"] else None
    user = requests.get(url=find_user_by(username=username)).json()
    karma = user["karma"] if user["karma"] else 0

    if karma < KARMA_LIMIT:
        resp.data = {"title": ""}
    else:
        print("story_id", data["id"], "user_id", data["by"])
        resp.data = resp.json()["title"]


class TenKKarmaStories(Resource):
    """Users 10.000 Karma Points Story API Endpoint."""

    def get(self):
        """
        GET-Method.

        :return: {dict} - 10 most frequent used words
        """
        titles = ""  # string representation of all titles

        new_stories_top500 = requests.get(url=newstories_url()).json()
        stories = new_stories_top500

        # Create the asynchronous session
        session = FuturesSession()

        res_stories = [
            session.get(url=story_url_for(story_id), hooks={"response": res_hook})
            for story_id in stories
        ]

        for story in res_stories:
            story = story.result()
            titles += f" {story.data}"

        return top_ten_words(titles)
