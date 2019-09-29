"""Response Hooks Utilities."""
import requests
from api_service.utilities.api_url import find_user_by
from settings import KARMA_LIMIT, ALLOWED_STORY_TYPES


def find_story_title_user_karma_hook(resp, *args, **kwargs):
    """
    Response hook.

    :param resp: {Response} - the response object from the ``session.get()``
    :param args: {tuple}
    :param kwargs: {dict}
    """
    data = resp.json()

    if "deleted" in data:
        resp.data = None
    else:
        username = data["by"] if data["by"] else None

        # TODO: handle duplicate users to reduce HN API queries
        user = requests.get(url=find_user_by(username=username)).json()
        karma = user["karma"] if user["karma"] else 0

        if karma < KARMA_LIMIT:
            resp.data = ""
        else:
            resp.data = data["title"]


def find_story_title_for_karma_hook(resp, *args, **kwargs):
    """
    Validate the response data.

    Set response data to the data of the response iff the response data contains the
    attribute ``type: story``, thus the data returned by the query is a story.

    :param resp: {Response} - response object from ``session.get()``
    :param args: {tuple}
    :param kwargs: {dict}
    """
    resp.data = None
    resp.data = resp.json()

    if resp.data is not None and resp.json()["type"] == "story":
        find_story_title_user_karma_hook(resp=resp)
    else:
        resp.data = None


def get_title_hook(resp, *args, **kwargs):
    """
    Validate the response object and set title as the response attribute.

    :param resp: {Response} - response object from ``session.get()`` function
    :param args: {tuple}
    :param kwargs: {dict}
    """
    resp.data = None  # initialize data attribute for response object resp
    data = resp.json()  # retrieve response json from response object

    # there might be items with an id but no content FTW!
    # eliminate items which have been deleted, since they don't contain a title
    if data is None or "deleted" in data and data["deleted"]:
        resp.data = None
    else:
        # TODO: add kwargs handler to overwrite the ALLOWED_STORY_TYPES manually
        #  maybe if one just want to get_titles_hook for only {type: story} only
        #  kwargs["only"] = ("story")
        if data["type"] in ALLOWED_STORY_TYPES:
            # check if item actually contains a title field
            resp.data = data["title"] if "title" in data else None
