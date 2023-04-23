from consts import *
from generate_posts import load_podcasts
from podcast_utils import get_thumbnail_url, save_podcasts


def main():
    podcasts, filtered_ids = load_podcasts()

    for id, podcast in podcasts.items():
        if podcast["thumbnail"] != "":
            # Skip podcasts that already have thumbnails
            continue

        podcast["thumbnail"] = get_thumbnail_url(podcast)

    save_podcasts(podcasts, filtered_ids)


if __name__ == "__main__":
    main()
