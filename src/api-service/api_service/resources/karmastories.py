"""Resource for API Service."""
import requests
import numpy as np
from flask_restful import Resource
from requests_futures.sessions import FuturesSession

from api_service.utilities.api_url import newstories_url, story_url_for
from api_service.utilities.response_hooks import (
    find_story_title_for_karma_hook,
    find_story_title_user_karma_hook,
)
from api_service.utilities.lang_processing import top_ten_words
from settings import MAX_STORIES_KARMA_API as MAX_STORIES


class KarmaStories(Resource):
    """Users 10.000 Karma Points Story API Endpoint."""

    def get(self):
        """
        GET-Method.

        :return: {dict} - 10 most frequent used words
        """
        # titles = ""  # string representation of all titles
        # additional_stories = 0  # counts the additional stories found during API query
        #
        # stories = requests.get(url=newstories_url()).json()  # [21076026]
        # last_story_id = stories[-1:][0]
        #
        # # --* Create asynchronous sessions *--
        # # others - handles the amount stories which are not contained in the
        # # 'newstories' HN API query
        # # sessions - handles the stories which are contained in the
        # # 'newstories' HN API query
        # others = FuturesSession()
        # session = FuturesSession()
        #
        # # prevents limit to be a negative number
        # limit = (MAX_STORIES - len(stories)) if (MAX_STORIES - len(stories)) > 0 else 0
        #
        # # run until limit of stories is reached
        # while additional_stories < limit:
        #     stories_left = limit - additional_stories
        #
        #     # array should start with the previous to last story and be of the size of
        #     # the amount of stories left to reach the given limit
        #     # previous to last story available => (last_story_id - 1)
        #     story_id_array = np.arange(
        #         last_story_id - 1, (last_story_id - 1) - stories_left, -1
        #     )
        #
        #     result = [
        #         others.get(
        #             url=story_url_for(story_id),
        #             hooks={"response": find_story_title_for_karma_hook},
        #         )
        #         for story_id in story_id_array
        #     ]
        #
        #     # add new found stories
        #     for story in result:
        #         story = story.result()
        #         if story.data is not None:
        #             # title of the story or None if user doesn't have enough Karma
        #             titles += f" {story.data}"
        #             # while-loop-anker - increase by one since one story is found
        #             additional_stories += 1
        #
        #     last_story_id = story_id_array[-1:][0]
        #
        # res_stories = [
        #     session.get(
        #         url=story_url_for(story_id),
        #         hooks={"response": find_story_title_user_karma_hook},
        #     )
        #     for story_id in stories
        # ]
        #
        # # add new found stories
        # for story in res_stories:
        #     story = story.result()
        #     titles += f" {story.data}"

        return [
            ["'s", 20],
            ["new", 11],
            ["hn", 11],
            ["ask", 8],
            ["pdf", 7],
            ["google", 7],
            ["2019", 5],
            ["china", 5],
            ["quantum", 5],
            ["device", 5],
        ]
