from os import environ
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Secrets
GOOGLE_API_KEY = environ.get('GOOGLE_API_KEY', "")

# Model
# MODEL_SIZE = "en_core_web_sm"  # small
MODEL_SIZE = "en_core_web_lg"  # large

# Links
URL = 'https://lexfridman.com'
FEED_URL = 'https://lexfridman.com/feed/podcast/'

# Schema
SCHEMA_PATH = 'schema'
PODCAST_SCHEMA_PATH = SCHEMA_PATH + '/podcast.json'
BOOK_SCHEMA_PATH = SCHEMA_PATH + '/book.json'

# File paths
OUTPUT_PATH = "out/"
PODCASTS_OUTPUT_PATH = OUTPUT_PATH + "podcasts.json"
BOOKS_OUTPUT_PATH = OUTPUT_PATH + "books.json"
TRANSCRIPTS_DIR_PATH = "../data/lexicap"
TRANSCRIPT_NAME_PREFIX = "episode_"
TRANSCRIPT_NAME_SUFFIX = ".txt"
POSTS_OUTPUT_PATH = "../site/src/posts"
POST_NAME_PREFIX = "ep_"
POST_NAME_SUFFIX = ".md"
