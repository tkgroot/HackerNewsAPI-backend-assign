"""API Service."""
import json
import math
import requests
import datetime
import numpy as np
from api_service.utilities.lang_processing import top_ten_words
from api_service.utilities.response_hooks import get_title_hook
from requests_futures.sessions import FuturesSession
from flask import Flask
from flask_restful import Resource, Api

from api_service.utilities.api_url import story_url_for, maxitem_url
from api_service.resources.twentyfivestories import TwentyFiveStories
from api_service.resources.tenkkarmastories import KarmaStories

app = Flask(__name__)
api = Api(app)


# helpers
def find_story_time_boundary(
    boundary, item, interval=240000, reverse=False, *args, **kwargs
):
    # set previous in kwargs to None in the beginning.
    # Its used for the recursive func to compare previous timestamp_diff with the new
    # timestamp_diff and is not required for the initial function call
    previous = kwargs["previous"] if "previous" in kwargs else None

    # convert boundary to int if string is passed. timestamp is normally of string type
    boundary = int(boundary) if isinstance(boundary, str) else boundary

    item = requests.get(url=story_url_for(item["id"])).json()
    item["time"] = int(
        datetime.datetime.utcfromtimestamp(item["time"])
        .replace(microsecond=0)
        .strftime("%s")
    )
    timestamp_diff = item["time"] - boundary

    if timestamp_diff == previous:
        return item

    if timestamp_diff < 0:
        previous = timestamp_diff if not reverse else previous
        item["id"] = item["id"] + interval
        return find_story_time_boundary(
            boundary, item, math.ceil(interval / 2), reverse, previous=previous
        )
    else:
        previous = timestamp_diff if reverse else previous
        item["id"] = item["id"] - interval
        return find_story_time_boundary(
            boundary, item, math.ceil(interval / 2), reverse, previous=previous
        )


# Resources
class SevenDaysStories(Resource):
    """7 Days API Endpoint."""

    def get(self):
        """
        Get-Method.

        :return:
        """
        titles = ""  # string representation of the titles
        item = {"id": requests.get(maxitem_url()).json()}  # set last item id from HN

        now = datetime.datetime.now().replace(microsecond=0)
        lb_timestamp = datetime.datetime(
            now.year, now.month, now.day - 7, second=1, tzinfo=datetime.timezone.utc
        ).strftime("%s")
        ub_timestamp = datetime.datetime(
            now.year,
            now.month,
            now.day - 7,
            hour=23,
            minute=59,
            second=59,
            tzinfo=datetime.timezone.utc,
        ).strftime("%s")

        upperbound_item = find_story_time_boundary(ub_timestamp, item)
        lowerbound_item = find_story_time_boundary(
            lb_timestamp, upperbound_item, interval=10000, reverse=True
        )

        stories_in_boundary = np.arange(lowerbound_item["id"], upperbound_item["id"], 1)

        # create query session and query the stories in stories_in_boundary
        session = FuturesSession()
        res_stories = [
            session.get(url=story_url_for(story_id), hooks={"response": get_title_hook})
            for story_id in stories_in_boundary
        ]

        # add new found stories titles and append them to titles
        for story in res_stories:
            story = story.result()
            if story.data is not None:
                titles += f" {story.data}"

        return top_ten_words(titles)


# Register API
api.add_resource(TwentyFiveStories, "/twenty_five_stories")
api.add_resource(SevenDaysStories, "/seven_days_stories")
api.add_resource(KarmaStories, "/karma_stories")

if __name__ == "__main__":
    app.run(debug=True)
