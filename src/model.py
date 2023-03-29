#model.py
import json
import spacy
import requests


from typing import List


MODEL_SIZE = "en_core_web_sm" # small
# MODEL = "en_core_web_lg"    # large


model = None
def extract_books(transcript: str) -> List[dict]:
    global model
    if model == None:
        model = spacy.load(MODEL_SIZE)

    doc = model(transcript)
    books = []
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
                    book_dict['authors'] = book['volumeInfo'].get('authors', ['']) #ran into this error, case where they don't have author
                    book_dict['isbn'] = book['volumeInfo'].get('industryIdentifiers', [{'identifier': ''}])[0]['identifier']
                    book_dict['image_url'] = book['volumeInfo'].get('imageLinks', {}).get('thumbnail')
                    book_dict['link'] = book['volumeInfo'].get('canonicalVolumeLink', '')
                    books.append(book_dict)
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
