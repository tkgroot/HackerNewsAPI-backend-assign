"""Response Hooks Utilities."""
import requests
import pprint
from api_service.utilities.api_url import find_user_by

# TODO: use .env for variable declaration instead
KARMA_LIMIT = 1000  # contains a constant for the karma limit
# contains the type of stories which titles are allowed to be processed
ALLOWED_STORY_TYPES = "story"


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
            print("story_id", data["id"], "user_id", data["by"])
            resp.data = resp.json()["title"]


def find_story_title_for_karma_hook(resp, *args, **kwargs):
    """
    Validate the response data.

    Set response data to the data of the response iff the response data contains the
    attribute ``type: story``, thus the data returned by the query is a story.
    """
    resp.data = resp.json()

    if resp.json()["type"] == "story":
        find_story_title_user_karma_hook(resp=resp)
    else:
        resp.data = None


def get_title_hook(resp, *args, **kwargs):
    """

    :param resp:
    :param args:
    :param kwargs:
    :return:
    """
    resp.data = None  # initialize data attribute for response object resp
    data = resp.json()  # retrieve response json from response object

    # There might be items with an id but no content FTW!
    if data is None or "deleted" in data:
        resp.data = None
    else:
        # TODO: add kwargs handler to overwrite the ALLOWED_STORY_TYPES manually
        #  maybe if one just want to get_titles_hook for only {type: story} only
        #  kwargs["only"] = ("story")
        if data["type"] in ALLOWED_STORY_TYPES:
            # double check if item actually contains a title field
            # print(resp.data["title"])
            resp.data = data["title"] if "title" in data else None
