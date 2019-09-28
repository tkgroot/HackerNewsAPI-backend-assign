"""HackerNews API - URL transformations."""
from api_service.settings import BASE_URL, API_VERSION


def newstories_url():
    """Generate the GETTER URL from HackerNews API to query new stories."""
    return f"{BASE_URL}/{API_VERSION}/newstories.json"


def story_url_for(idx=None):
    """Generate the GETTER URL from HackerNews API for stories."""
    if idx is None:
        return None

    return f"{BASE_URL}/{API_VERSION}/item/{idx}.json"


def find_user_by(username=None):
    """Generate the GETTER URL from HN API to query the user data for given user."""
    if username is None:
        return None

    return f"{BASE_URL}/{API_VERSION}/user/{username}.json"


def maxitem_url():
    """Generate the GETTER URL from HN API to query the maxitem."""
    return f"{BASE_URL}/{API_VERSION}/maxitem.json"
