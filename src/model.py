import consts

from podcast_utils import *

import spacy
from spacy.language import Language
from spacy.tokens import Doc


def get_book_schema() -> object:
    """
    Load the book JSON schema into an object
    """
    with open(consts.book_schema_path, 'r') as read_file:
        schema = json.load(read_file)
    return schema


def get_transcript_path(transcript_name: str) -> str:
    """
    Get full path to transcript
    """
    path = consts.transcripts_path + "/" + transcript_name
    return path


def get_transcript_name(num: int) -> str:
    """
    Get transcript file name by number/ID
    """
    name = consts.transcript_name_prefix + \
        str(num) + consts.transcript_name_suffix
    return name


def init_spacy() -> Language:
    """
    Initaliaze spacy
    """
    nlp = spacy.load("en_core_web_sm")
    return nlp


def tokenize_transcript(nlp: Language, transcript: str) -> Doc:
    """
    Tokenize podcast transcript; returns spacy document
    """
    doc = nlp(transcript)
    return doc


def get_book_recommendations(transcript: str):
    """
    Get book recommendations from podcast transcript
    """
    return NotImplemented


if __name__ == "__main__":
    book = get_book_schema()

