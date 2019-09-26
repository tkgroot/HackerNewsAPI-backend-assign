"""HackerNews API - URL transformations."""
BASE_URL = "https://hacker-news.firebaseio.com/"
API_V = 0


def newstories_url():
    """Generate the GETTER URL from HackerNews API to query new stories."""
    return f"{BASE_URL}/v{API_V}/newstories.json"


def story_url_for(idx=None):
    """Generate the GETTER URL from HackerNews API for stories."""
    if idx is None:
        return None

    return f"{BASE_URL}/v{API_V}/item/{idx}.json"


def find_user_by(username=None):
    """Generate the GETTER URL from HN API to query the user data for given user."""
    if username is None:
        return None

    return f"{BASE_URL}/v{API_V}/user/{username}.json"
