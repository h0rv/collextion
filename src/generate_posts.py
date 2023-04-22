#generate_posts.py
import json
import googleapiclient.discovery
from operator import itemgetter

from pytablewriter import MarkdownTableWriter

from consts import *


def load_podcasts() -> dict:
    """
    Load the podcast list JSON into an object
    """
    podcasts_path = PODCASTS_OUTPUT_PATH
    with open(podcasts_path, 'r') as read_file:
        podcasts = json.load(read_file)
    return podcasts


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

    thumbnail_url = get_thumbnail(podcast)  # call the get_thumbnail() function
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



def get_thumbnail(podcast):
    # Build the search query for the YouTube Data API
    search_query = podcast['title'] + ' podcast'
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey='AIzaSyATEUvdIpco20xGb_zojSJxNZkX9u7Xcys')
    request = youtube.search().list(
        q=search_query,
        type='video',
        part='snippet',
        maxResults=1
    )
    response = request.execute()
    video_id = response['items'][0]['id']['videoId']

    # Construct the thumbnail URL
    thumbnail_url = 'https://img.youtube.com/vi/{}/maxresdefault.jpg'.format(video_id)

    return thumbnail_url


def write_podcast_info(file, podcast):
    heading = '\n# ' + podcast['title'] + '\n\n'
    file.write(heading)

    date = '  - Date: ' + podcast['date'] + '\n'
    file.write(date)
    date = '  - Link: ' + podcast['url'] + '\n'
    file.write(date)
    date = '  - Description: ' + podcast['description'] + '\n'
    file.write(date)


'''
def write_book_recommendations(file, recommendations):
    heading = '\n## Book Recommendations\n\n'
    file.write(heading)
    try:                                    #catch an error I got during runtime, use utf-8 format
        file.write(str(recommendations))
    except UnicodeEncodeError as e:
        print(f"Caught UnicodeEncodeError: {e}")
        recommendations_str = str(recommendations).encode("utf-8", errors="ignore").decode()
        file.write(recommendations_str)
    # 
    # writer = MarkdownTableWriter(
    #     table_name="example_table",
    #     headers=["int", "float", "str", "bool", "mix", "time"],
    #     value_matrix=[
    #         [0,   0.1,      "hoge", True,   0,      "2017-01-01 03:04:05+0900"],
    #     ],
    # )
    # writer.write_table()
    # writer.close()
'''

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
        file.write(f'<td style="border: none;"><img src="{cover}" alt="{title}" width="150" style="vertical-align: top;"></td>')
        file.write('<td style="border: none; vertical-align: top;">')
        file.write(f"<h3 style='margin-top: 5'>{title}</h3>")
        file.write(f"<p><strong>Author:</strong> {author}</p>")
        file.write(f"<p><strong>ISBN:</strong> {isbn}</p>")
        file.write(f'<p><strong>Book URL:</strong> <a href="{book_url}">{book_url}</a></p>')
        file.write('</td></tr></table>\n')

from operator import itemgetter

def print_recommended_books(recommendations, podcast):
    recommended_books = []
    for recommendation in recommendations:
        book = recommendation['book_title']
       # podcast = recommendation['podcast']
        found = False
        # Check if book is already in recommended_books list
        for i, rec in enumerate(recommended_books):
            if rec[0] == book:
                found = True
                recommended_books[i][1].append(podcast)
                recommended_books[i][2] += 1
                break
        # If book is not already in recommended_books list, add it
        if not found:
            recommended_books.append([book, [podcast], 1])

    # Sort recommended_books list by number of recommendations (descending)
    recommended_books.sort(key=itemgetter(2), reverse=True)

    recommended_books_dict = {rec[0]: {'podcasts': rec[1], 'num_recommendations': rec[2]} for rec in recommended_books}

    with open('most_recommended_books.json', 'w') as f:
         json.dump(recommended_books_dict, f)
    #return recommended_books

    # Print out recommended books with book cover and podcasts that recommended it
    '''
    for book, podcasts, count in recommended_books:
        print(f"{book}\n")
        print(f"{count} recommendations")
        for podcast in podcasts:
            print(f"Recommended by {podcast}")
        print("\n")
    '''

    # Print out recommended books with book cover and podcasts that recommended it
 
def main():
    podcasts = load_podcasts()
    books_list = load_books()

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

        print_recommended_books(recommendations, podcast)
     #   get_thumbnail(podcast)

        file.close()


if __name__ == "__main__":
    main()