import json
import feedparser

from consts import *


def get_podcast_schema() -> dict:
    """
    Load the podcast JSON schema into an object
    """
    with open(PODCAST_SCHEMA_PATH, 'r') as read_file:
        schema = json.load(read_file)
    return schema


def get_rss_feed():
    """
    Get RSS feed for the podcast
    """
    feed = feedparser.parse(FEED_URL)
    return feed


def get_podcast_entries() -> list[object]:
    """
    Get podcast entries from RSS feed
    """
    feed = get_rss_feed()
    podcast_entries = feed['entries']
    return podcast_entries


def get_title(entry: dict) -> str:
    """
    Get title of podcast
    """
    title = entry['title']
    return title


def get_podcast_number(entry: dict) -> int:
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
    return int(num)


def get_guest_name(entry: dict) -> str:
    """
    Get guest name from link
        Example: `https://lexfridman.com/max-tegmark/`
    """
    link = entry['link']
    name = link.replace(URL, '')
    name = name.replace('-', ' ')
    # Get rid of non-alphabetic characters besides ' '
    name = ''.join([c for c in name if c.isalpha() or c == ' ']).strip()
    # Capitalize name
    name = name.strip()
    return name


def get_date(entry: dict) -> str:
    """
    Get date of publication
    """
    parsed_date = entry['published_parsed']
    year = str(parsed_date[0])
    month = str(parsed_date[1])
    day = str(parsed_date[2])
    return month + '/' + day + '/' + year


def get_url(entry: dict) -> str:
    """
    Get link to podcast
    """
    url = entry['link']
    return url


def get_mp3_url(entry: dict) -> str:
    """
    Get link to MP3 to podcast
    """
    url = ""

    links = entry['links']
    for link in links:
        if link['type'] == 'audio/mpeg':
            url = link['href']
            break

    return url


def get_description(entry: dict) -> str:
    """
    Get description of podcast
    """
    description = entry['summary']
    first_linebreak = description.find('<br />')
    description = description[:first_linebreak] # Get only first paragraph
    return description


def extract_podcast_info(entry) -> dict:
    """
    Extract information into JSON from a podcast RSS entry
    """
    info = get_podcast_schema()

    info['title'] = get_title(entry)
    info['id'] = get_podcast_number(entry)
    info['guest'] = get_guest_name(entry)
    info['date'] = get_date(entry)
    info['url'] = get_url(entry)
    info['mp3'] = get_mp3_url(entry)
    info['description'] = get_description(entry)

    return info


def main():
    entries = get_podcast_entries()

    info_map = dict()
    for entry in entries:
        info = extract_podcast_info(entry)
        id = info['id']
        info_map[id] = info

    with open(PODCASTS_OUTPUT_PATH, 'w') as f:
        json.dump(info_map, f)


if __name__ == "__main__":
    main()
