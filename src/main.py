#!/bin/python3


from podcast_utils import main as podcasts
from book_utils import main as books
from generate_posts import main as posts


def main():
    podcasts()
    books()
    posts()


if __name__ == "__main__":
    main()
