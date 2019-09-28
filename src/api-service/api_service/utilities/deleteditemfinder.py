"""Utility Functions."""
import requests
from api_service.utilities.api_url import story_url_for


def find_deleted_item(item):
    """
    Iterate through the items list finding an item with deleted flag set to True.

    Iterates from a given starting point through the items of the HackerNews items
    evaluating each item if the deleted flag ``{deleted: True}`` is set. If this item
    is found it is then returned. Otherwise this function continues by decreasing the
    item's id by one.

    :param item: HN item
    :return: HN item - item contains the flag ``{deleted: True}``
    """
    item = requests.get(story_url_for(item["id"])).json()
    if item["id"] % 10 == 0:
        print(item["id"])
    if "deleted" in item and item["deleted"]:
        print(item)
        return item
    else:
        item["id"] -= 1
        find_deleted_item(item)
