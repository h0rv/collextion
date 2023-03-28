import json
import spacy

from typing import List


MODEL_SIZE = "en_core_web_sm" # small
# MODEL = "en_core_web_lg"    # large


model = None
def extract_books(transcript: str) -> List[str]:
    global model
    if model == None:  # avoid reloading model for each transcript
        model = spacy.load(MODEL_SIZE)

    doc = model(transcript)
    books = []
    for ent in doc.ents:
        if ent.label_ == "WORK_OF_ART":
            book = ent.text
            books.append(book)

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
