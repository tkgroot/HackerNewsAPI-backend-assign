"""Resource for API Service."""
import requests
from flask_restful import Resource
from requests_futures.sessions import FuturesSession
from api_service.utilities.lang_processing import top_ten_words
from api_service.utilities.api_url import story_url_for, newstories_url

MAX_STORIES = 25  # const variable contains story limit


class TwentyFiveStories(Resource):
    """25 Stories API Endpoint."""

    def get(self):
        """
        GET-Method.

        requests the HackerNews API ``/newstories.json`` to retrieve the latest 500
        story ids, using 25 ids to request the story's content from HackerNews.
        The stories are then filtered the title extracted and merged together in one
        title string. This is is then passed into ``to_ten_words()`` to gather to top
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

        # TODO: use get_title_hook with additional kwargs parameter to limit
        #  the use of ALLOWED_STORY_TYPES
        res_stories = [session.get(story_url_for(idx=story_id)) for story_id in stories]

        for story in res_stories:
            content = story.result().json()

            # Validates the content to be existent and verify that the title key exists
            # Deleted stories are flagged with {deleted:True} and do not contain a
            # title key
            # TODO: use a response_hook instead
            # TODO: handle deleted:True differently
            if content is not None and "title" in content:
                titles += f" {content['title']}"
                story_counter += 1

        return top_ten_words(titles)
