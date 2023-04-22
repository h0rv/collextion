from os import environ, path
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

cwd = path.dirname(__file__)

# Secrets
GOOGLE_API_KEY = environ.get("GOOGLE_API_KEY", "")

# Model
# MODEL_SIZE = "en_core_web_sm"  # small
MODEL_SIZE = "en_core_web_lg"  # large

# Links
URL = "https://lexfridman.com"
FEED_URL = "https://lexfridman.com/feed/podcast/"

# Schema
SCHEMA_PATH = path.join(cwd, "..", "schema")
PODCAST_SCHEMA_PATH = path.join(SCHEMA_PATH, "podcast.json")
BOOK_SCHEMA_PATH = path.join(SCHEMA_PATH, "book.json")

# File paths
OUTPUT_PATH = path.join(cwd, "out")
PODCASTS_OUTPUT_PATH = path.join(OUTPUT_PATH, "podcasts.json")
BOOKS_OUTPUT_PATH = path.join(OUTPUT_PATH, "books.json")
PROCESSED_PODCASTS_FILE = path.join(OUTPUT_PATH, "processed.json")
TRANSCRIPTS_DIR_PATH = path.join(cwd, "..", "data", "lexicap")
TRANSCRIPT_NAME_PREFIX = "episode_"
TRANSCRIPT_NAME_SUFFIX = ".txt"
POSTS_OUTPUT_PATH = path.join(cwd, "..", "site", "src", "posts")
POST_NAME_PREFIX = "ep_"
POST_NAME_SUFFIX = ".md"
MOST_RECOMMENDED_PATH = "most_recommended_books.json"
