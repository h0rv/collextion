import json
import feedparser


url = 'https://lexfridman.com'
feed_url = 'https://lexfridman.com/feed/podcast/'
schema_path = '../schema'
podcast_schema_path = schema_path + '/podcast.json'
output_file_path = "podcasts.json"


def get_podcast_schema():
    """
    Load the podcast JSON schema into an object
    """
    with open(podcast_schema_path, 'r') as read_file:
        schema = json.load(read_file)
    return schema


def get_rss_feed():
    """
    Get RSS feed for the podcast
    """
    feed = feedparser.parse(feed_url)
    return feed


def get_podcast_entries():
    """
    Get podcast entries from RSS feed
    """
    feed = get_rss_feed()
    podcast_entries = feed['entries']
    return podcast_entries


def get_title(entry):
    """
    Get title of podcast
    """
    title = entry['title']
    return title


def get_podcast_number(entry):
    """
    Get number of the podcast
    """
    title = get_title(entry)

    try:
        start = title.index('#') + 1  # skip over '#'
    except ValueError:
        """
        TODO - implement for older episodes that do are not numbered
        """
        return -1

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
    name = ''.join([c for c in name if c.isalpha() or c == ' ']).strip()
    # Capitalize name
    name = name.strip()
    return name


def get_date(entry):
    """
    Get date of publication
    """
    parsed_date = entry['published_parsed']
    year = str(parsed_date[0])
    month = str(parsed_date[1])
    day = str(parsed_date[2])
    return month + '/' + day + '/' + year


def get_url(entry):
    """
    Get link to podcast
    """
    url = entry['link']
    return url


def get_description(entry):
    """
    Get description of podcast
    """
    description = entry['summary']
    return description


def extract_podcast_info(entry):
    """
    Extract information into JSON from a podcast RSS entry
    """
    info = get_podcast_schema()

    info['title'] = get_title(entry)
    info['id'] = get_podcast_number(entry)
    info['guest'] = get_guest_name(entry)
    info['date'] = get_date(entry)
    info['url'] = get_url(entry)
    info['description'] = get_description(entry)

    return info


if __name__ == "__main__":
    entries = get_podcast_entries()

    info_map = dict()
    for entry in entries:
        info = extract_podcast_info(entry)
        id = info['id']
        info_map[id] = info

    with open(output_file_path, 'w') as f:
        json.dump(info_map, f)

