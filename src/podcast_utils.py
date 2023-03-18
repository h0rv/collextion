import json
import feedparser


url = 'https://lexfridman.com'
feed_url = 'https://lexfridman.com/feed/podcast/'
schema_path = '../schema'
podcast_schema_path = schema_path + '/podcast.json'


def get_title(entry):
    """
    Get title of podcast
    """
    title = entry['title']
    return title


def get_podcast_number(entry):
    """
    TODO - implement for older episodes that do are not numbered
    """
    title = get_title(entry)
    start = title.index('#') + 1  # skip over '#'
    end = title.index(' ', start)
    num = title[start:end]
    return num


def get_guest_name(entry):
    """
    Get guest name from link
        Example: `https://lexfridman.com/max-tegmark/`
    """
    link = entry['link']
    name = link.replace(url, '')
    name = name.replace('-', ' ')
    # Get rid of non-alphabetic characters besides ' '
    name = ''.join([c for c in name if c.isalpha() or c == ' '])
    # Capitalize name
    name = name.title()
    return name


def extract_podcast_info(entry):
    """
    Extract information into JSON from a podcast RSS entry
    """
    json = get_podcast_schema()

    json['title'] = get_title(entry)
    json['id'] = get_podcast_number(entry)
    json['guest'] = get_guest_name(entry)

    print(json['id'])
    return NotImplemented


def get_podcast_schema():
    """
    Load the podcast JSON schema into an object
    """
    with open(podcast_schema_path, 'r') as read_file:
        schema = json.load(read_file)
    return schema


def get_podcast_entries():
    """
    Get podcast entries from RSS feed
    """
    feed = get_rss_feed()
    podcast_entries = feed['entries']
    return podcast_entries


def get_rss_feed():
    """
    Get RSS feed for the podcast
    """
    feed = feedparser.parse(feed_url)
    return feed


if __name__ == "__main__":
    entries = get_podcast_entries()
    extract_podcast_info(entries[0])
