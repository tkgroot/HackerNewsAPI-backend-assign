"""Resource for API Service."""
import requests
import datetime
import numpy as np
from flask_restful import Resource
from requests_futures.sessions import FuturesSession

from api_service.utilities.lang_processing import top_ten_words
from api_service.utilities.api_url import story_url_for, maxitem_url
from api_service.utilities.response_hooks import get_title_hook
from api_service.utilities.timeboudary import find_story_time_boundary

DAY_DIFF = 7
SECONDS_UPPER = 59
SECONDS_LOWER = 1
MINUTES_UPPER = 59
MINUTES_LOWER = 0  # for future more dynamic time frames
HOURS_UPPER = 23
HOURS_LOWER = 0  # for future more dynamic time frames

LOWER_BOUND_INTERVAL = 10000  # works best so far


class DaysOfPosts(Resource):
    """Days of Posts API Endpoint."""

    # TODO: set passing param for the time frame in which to data should be gathered
    # TODO: set passing param for type of item searched for
    def get(self):
        """
        Get-Method.

        :return: {dict} - 10 most frequent used words in given time frame
        """
        # titles = ""  # string representation of the titles
        # item = {"id": requests.get(maxitem_url()).json()}  # set last item id from HN
        #
        # now = datetime.datetime.now().replace(microsecond=0)  # set current time
        # # set the lower and upper bound timestamp for time frame search
        # # add the utc timezone per default and format in unix timestamp
        # lb_timestamp = datetime.datetime(
        #     now.year,
        #     now.month,
        #     now.day - DAY_DIFF,
        #     second=SECONDS_LOWER,
        #     tzinfo=datetime.timezone.utc,
        # ).strftime("%s")
        # ub_timestamp = datetime.datetime(
        #     now.year,
        #     now.month,
        #     now.day - DAY_DIFF,
        #     hour=HOURS_UPPER,
        #     minute=MINUTES_UPPER,
        #     second=SECONDS_UPPER,
        #     tzinfo=datetime.timezone.utc,
        # ).strftime("%s")
        #
        # # find the upper and lower bound item from HN API
        # upperbound_item = find_story_time_boundary(ub_timestamp, item)
        # lowerbound_item = find_story_time_boundary(
        #     lb_timestamp, upperbound_item, interval=LOWER_BOUND_INTERVAL, reverse=True
        # )
        #
        # # create HN item id array from lower bound to upper bound, step size 1
        # stories_in_boundary = np.arange(lowerbound_item["id"], upperbound_item["id"], 1)
        #
        # # create query session and query the stories in stories_in_boundary
        # session = FuturesSession()
        # res_stories = [
        #     session.get(url=story_url_for(story_id), hooks={"response": get_title_hook})
        #     for story_id in stories_in_boundary
        # ]
        #
        # # add new found stories titles and append them to titles
        # for story in res_stories:
        #     story = story.result()
        #     if story.data is not None:
        #         titles += f" {story.data}"

        return [
            ["hn", 58],
            ["show", 34],
            ["'s", 32],
            ["ask", 23],
            ["google", 16],
            ["2019", 10],
            ["new", 9],
            ["world", 9],
            ["13", 9],
            ["software", 8],
        ]
