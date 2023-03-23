from spacy.training import Example
from spacy.tokens import DocBin
import spacy
import json
from tqdm import tqdm
import random

def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def save_data(file, data):
    with open(file, "w",encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def test_model(model, text):
    doc = nlp(text)
    results = []
    for ent in doc.ents:
        results.append(ent.text)
    return results

nlp = spacy.blank("en")
ner = nlp.add_pipe("ner")

book_labels = ["BOOK"]

book_train = load_data("/Users/erastoomolo/Desktop/CS1699/collextion/src/training.json")

# Create a new list to store the converted data
converted_data = []

# Loop through each item in the JSON file and extract the relevant information
for item in book_train:
    text = item["text"]
    entities = ((e["start"], e["end"], e["label"]) for e in item["entities"])
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, {"entities": entities})
    converted_data.append(example)

# Add the book label to the NER model
for label in book_labels:
    ner.add_label(label)

# Train the NER model on the training data
optimizer = nlp.begin_training()
for i in range(10):
    random.shuffle(converted_data)
    doc_bin = DocBin() 
    for item in converted_data:
        doc_bin.add(item)
        
    doc_bin = doc_bin.to_bytes()
    doc_bin = DocBin().from_bytes(doc_bin)
    for batch in spacy.util.minibatch(doc_bin.get_docs(nlp.vocab), size=4):
        nlp.update(batch, sgd=optimizer)
