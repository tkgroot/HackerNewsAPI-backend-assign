"""System Settings."""
import os
from dotenv import load_dotenv

# load environment variables into settings
load_dotenv()


# --* Default Settings *--
BASE_URL = os.getenv("BASE_URL", "https://hacker-news.firebaseio.com")  # URL from HN
API_VERSION = os.getenv("API_VERSION", "v0")


# --* FLASK Settings *--
FLASK_APP = os.getenv("FLASK_APP", "api.py")
FLASK_ENV = os.getenv("FLASK_ENV", "development")
FLASK_DEBUG = os.getenv("FLASK_DEBUG", None)

# --* API Service Settings *--
KARMA_LIMIT = int(os.getenv("KARMA_LIMIT", 10000))
MAX_STORIES_KARMA_API = int(os.getenv("MAX_STORIES_KARMA_API", 600))
MAX_STORIES_API = int(os.getenv("MAX_STORIES_API", 25))
# contains the type of stories which titles are allowed to be processed
ALLOWED_STORY_TYPES = os.getenv("ALLOWED_STORY_TYPES", "story").split(",")


# --* Language Processing *--
SPECIAL_CHARS = "" + os.getenv("SPECIAL_CHARS", "'´”`–“``’‘")
