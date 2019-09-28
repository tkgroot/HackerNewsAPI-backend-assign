"""Time Boundary Utility Functions."""
import math
import datetime
import requests

from api_service.utilities.api_url import story_url_for


def find_story_time_boundary(
    boundary, item, interval=240000, reverse=False, *args, **kwargs
):
    """
    Find the story for a given time.

    the reverse param defines if the closest item should be bigger or smaller then the
    boundary passed as function parameter.

    :param boundary: {str} - unix timestamp to search for
    :param item: {dict} - HackerNews item as reference starting point
    :param interval: {int} - size of interval
    :param reverse: {boolean} - defines which item should be selected, by defining the
            upper and lower bound
    :param args: {tuple}
    :param kwargs: {dict}
    :return: {dict} item - HackerNews item which matches the time frame.
    """
    # set previous in kwargs to None in the beginning.
    # Its used for the recursive func to compare previous timestamp_diff with the new
    # timestamp_diff and is not required for the initial function call
    previous = kwargs["previous"] if "previous" in kwargs else None

    # convert boundary to int if string is passed. timestamp is normally of string type
    boundary = int(boundary) if isinstance(boundary, str) else boundary

    # query the item passed and retrieve content from the HN API
    item = requests.get(url=story_url_for(item["id"])).json()

    # update the unix timestamp from the item by removing the microseconds
    item["time"] = int(
        datetime.datetime.utcfromtimestamp(item["time"])
        .replace(microsecond=0)
        .strftime("%s")
    )
    timestamp_diff = item["time"] - boundary  # calculate the timestamp difference

    # recursive-func-anker
    # if the previous timestamp matches the current timestamp then this is the smallest
    # time difference an item on HackerNews can have
    if timestamp_diff == previous:
        return item

    if timestamp_diff < 0:
        # set previous to current timestamp difference iff upper bound should be used
        previous = timestamp_diff if not reverse else previous
        item["id"] = item["id"] + interval  # add interval to item id to increase id
        return find_story_time_boundary(
            boundary, item, math.ceil(interval / 2), reverse, previous=previous
        )
    else:
        # set previous to current timestamp difference iff lower bound should be used
        previous = timestamp_diff if reverse else previous
        item["id"] = item["id"] - interval  # subtract interval to decrease item id
        return find_story_time_boundary(
            boundary, item, math.ceil(interval / 2), reverse, previous=previous
        )
