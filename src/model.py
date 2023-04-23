import json

from consts import *

import requests
import spacy


model = None


def extract_books(transcript: str) -> [dict]:
    global model
    if model is None:
        model = spacy.load(MODEL_SIZE)

    doc = model(transcript)
    books = []
    titles_seen = set()
    for ent in doc.ents:
        if ent.label_ == "WORK_OF_ART":
            book_title = ent.text
            # Call Google Books API to get book details
            url = f"https://www.googleapis.com/books/v1/volumes?q={book_title}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if "items" in data:
                    # Get the first item in the list of books returned by the API
                    book = data["items"][0]
                    # Extract book details
                    book_dict = {}
                    book_dict['title'] = book['volumeInfo']['title']
                    if book_dict['title'] in titles_seen:
                        # Skip duplicate
                        continue
                    # ran into this error, case where they don't have author
                    book_dict['authors'] = book['volumeInfo'].get(
                        'authors', [''])
                    book_dict['isbn'] = book['volumeInfo'].get(
                        'industryIdentifiers', [{'identifier': ''}])[0]['identifier']
                    book_dict['image_url'] = book['volumeInfo'].get(
                        'imageLinks', {}).get('thumbnail')
                    book_dict['link'] = book['volumeInfo'].get(
                        'canonicalVolumeLink', '').replace("http://", "https://")

                    # Convert links to https
                    img_url = book_dict['image_url']
                    if img_url != '' and img_url is not None:
                        book_dict['image_url'] = img_url.replace(
                            "http://", "https://")
                    book_url = book_dict['link']
                    if book_url != '' and book_url is not None:
                        book_dict['link'] = book_url.replace(
                            "http://", "https://")

                    books.append(book_dict)
                    titles_seen.add(book_dict['title'])
    return books


def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def save_data(file, data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def test_model(model, text):
    doc = model(text)
    results = []
    for ent in doc.ents:
        results.append(ent.text)
    return results


def test():
    transcript = "The following is a conversation with Rana L. Kliubi, a pioneer in the field of emotion recognition and human centric artificial intelligence. She is the founder of Effectiva, deputy CEO of SmartEye, author of Girl Decoded ,and one of the most brilliant, kind, inspiring, and fun human beings I've gotten the chance to talk to. This is the Lex Freidman podcast"
    book_title_list = extract_books(transcript)
    print(book_title_list)


if __name__ == "__main__":
    test()
