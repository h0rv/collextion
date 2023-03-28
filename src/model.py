import spacy
import json
from book_utils import get_transcript_path
from spacy.training import Example
from spacy.tokens import DocBin


def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def save_data(file, data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def test_model(nlp, text):
    doc = nlp(text)
    results = []
    for ent in doc.ents:
        results.append(ent.text)
    return results


def extract_title_list(transcript):
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(transcript)
    book_title_list = []
    for ent in doc.ents:
        if ent.label_ == "WORK_OF_ART":
            book_name = ent.text
            book_title_list.append(book_name)
    return book_title_list


def test():
    transcript = "The following is a conversation with Rana L. Kliubi, a pioneer in the field of emotion recognition and human centric artificial intelligence. She is the founder of Effectiva, deputy CEO of SmartEye, author of Girl Decoded ,and one of the most brilliant, kind, inspiring, and fun human beings I've gotten the chance to talk to. This is the Lex Freidman podcast"
    book_title_list = extract_title_list(transcript)
    print(book_title_list)


if __name__ == "__main__":
    test()

