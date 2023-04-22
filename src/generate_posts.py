import json

from datetime import datetime

from consts import *


def load_podcasts() -> (dict, [int]):
    """
    Load the podcast list JSON into an object
    """
    podcasts_path = PODCASTS_OUTPUT_PATH
    with open(podcasts_path, 'r') as read_file:
        podcasts = json.load(read_file)

    return podcasts["podcasts"], podcasts["filtered_ids"]


def load_books() -> dict:
    """
    Load the books list JSON into an object
    """
    books_path = BOOKS_OUTPUT_PATH
    with open(books_path, 'r') as read_file:
        books = json.load(read_file)
    return books


def get_post_filename(id):
    name = POSTS_OUTPUT_PATH + '/' + POST_NAME_PREFIX + id + POST_NAME_SUFFIX
    return name


def create_post_file(id):
    name = get_post_filename(id)
    f = open(name, 'w')
    return f


def write_yaml_block(file, podcast):
    block = '---\n'

    file.write(block)
    # Body of block
    title = 'title: ' + '"' + podcast['title'] + '"\n'
    file.write(title)

    # TODO: Remove line breaks better in description (breaks the YAML)
    description = 'description: |\n' + "  " + podcast['description'] + '"\n'
    file.write(description)

    thumbnail_url = podcast['thumbnail']
    thumbnail_path = 'thumb: ' + '"' + thumbnail_url + '"\n'
    file.write(thumbnail_path)

    # TODO: Wasn't working with 11ty template
    # date = 'date: ' + '"' + podcast['date'] + '"\n'
    # file.write(date)

    # TODO
    # tags = 'tags: '
    # file.write(tags)
    # for tag in tag_list:
    #     prefix = "   - "
    #     tag = prefix + '\'' + tag + '\''
    #     file.write(tag)

    file.write(block)


def write_podcast_info(file, podcast):
    heading = '\n# ' + podcast['title'] + '\n\n'
    file.write(heading)

    date = '  - Date: ' + podcast['date'] + '\n'
    file.write(date)
    date = '  - Link: ' + podcast['url'] + '\n'
    file.write(date)
    date = '  - Description: ' + podcast['description'] + '\n'
    file.write(date)


def write_book_recommendations(file, recommendations):
    heading = '\n## Book Recommendations\n\n'
    file.write(heading)

    for book in recommendations:
        title = f"{book['book_title']}"
        author = f"{book['book_author']}"
        cover = f"{book['book_cover']}"
        isbn = f"{book['ISBN']}"
        book_url = f"{book['book_link']}"

        # Write each book's information with cover image and text in two columns
        file.write('<table style="border: none;"><tr style="border: none;">')
        file.write(
            f'<td style="border: none;"><img src="{cover}" alt="{title}" width="150" style="vertical-align: top;"></td>')
        file.write('<td style="border: none; vertical-align: top;">')
        file.write(f"<h3 style='margin-top: 5'>{title}</h3>")
        file.write(f"<p><strong>Author:</strong> {author}</p>")
        file.write(f"<p><strong>ISBN:</strong> {isbn}</p>")
        file.write(
            f'<p><strong>Book URL:</strong> <a href="{book_url}">{book_url}</a></p>')
        file.write('</td></tr></table>\n')


def main():
    podcasts, filtered_ids = load_podcasts()
    books_list = load_books()

    # Append to already filtered out podcasts
    processed_podcast_ids = filtered_ids

    for id, books in books_list.items():
        # Skip if no corresponding podcast
        if id not in podcasts:
            continue

        recommendations = books['recommendations']
        podcast = podcasts[id]

        # Create file
        file = create_post_file(id)

        write_yaml_block(file, podcast)
        write_podcast_info(file, podcast)
        write_book_recommendations(file, recommendations)

        # Add podcast to processed list
        processed_podcast_ids += id

        file.close()

    with open(PROCESSED_PODCASTS_FILE, "w") as f:
        json.dump({
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "podcast_ids": processed_podcast_ids,
        }, f)


if __name__ == "__main__":
    main()
