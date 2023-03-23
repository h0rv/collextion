from tqdm import tqdm
import spacy
from spacy.tokens import DocBin
import os

TRAIN_DATA = [("The following is a conversation with Stuart Russell. He's a professor of computer science at UC Berkeley and a coauthor of a book that introduced me and millions of other people to the amazing world of AI called Artificial Intelligence, A Modern Approach. This is the Lex Fridman podcast", {'entities':[(4,7,'BOOK')]}),
("The following is a conversation with Ray Dalio, his second time on the podcast. He is a legendary investor, founder of Bridgewater Associates, author of a book I highly recommend called Principles,and also a new book called Principles for Dealing with a Changing World Order. This is the Lex Friedman podcast", {'entities':[(100,109,'BOOK'), (128,161,'BOOK')]}),
("The following is a conversation with Nick Lane, a biochemist at University College London and author of some of my favorite books on biology, science, and life ever written, including his two most recent titled Transformer, The Deep Chemistry of Life and Death, and the vital question, why is life the way it is? This is the Lex Fridman podcast.", {'entities':[(124,156,'BOOK'), (38,63,'BOOK'), (68,81,'BOOK'), (86,107,'BOOK')]}),
("The following is a conversation with Rana L. Kliubi, a pioneer in the field of emotion recognition and human centric artificial intelligence. She is the founder of Effectiva, deputy CEO of SmartEye, author of Girl Decoded, and one of the most brilliant, kind, inspiring, and fun human beings I've gotten the chance to talk to. This is the Lex Freidman podcast", {'entities':[(69,81,'BOOK')]}),
("The following is a conversation with Jordan Peterson, an influential psychologist, lecturer, podcast host, and author of Maps of Meaning, 12 Rules for Life, and Beyond Order. This is the Lex Freidman podcast", {'entities':[(26,39,'BOOK'), (44,57,'BOOK'), (62,74,'BOOK')]}),
("He has written several books I recommend, including The New Economics and Manifesto and Debunking Economics. This is the Lex Friedman Podcast.", {'entities':[(33,52,'BOOK'), (57,74,'BOOK')]}),
("The following is a conversation with Jack Barsky, a former KGB spy, author of Deep Undercover and the subject of an excellent podcast series called The Agent.", {'entities':[(34,49,'BOOK')]}),
("The following is a conversation with Neil deGrasse Tyson, astrophysicist and author of Astrophysics for People in a Hurry. This is the Lex Freedman podcast.", {'entities':[(43,74,'BOOK')]}),
("The following is a conversation with Dan Brown, bestselling author of The Da Vinci Code and Inferno. This is the Lex Fredman podcast.", {'entities':[(28,46,'BOOK'), (51,58,'BOOK')]}),
("The following is a conversation with Eric Schmidt, former CEO of Google and co-author of The New Digital Age. This is the Lux Fridman podcast.", {'entities':[(65,83,'BOOK')]}),
("The following is a conversation with Steven Pinker, cognitive psychologist and author of The Blank Slate and Enlightenment Now. This is the Lex Reedman podcast.", {'entities':[(51,64,'BOOK'), (69,85,'BOOK')]}),
("The following is a conversation with Michelle Obama, former First Lady of the United States and author of Becoming, and this is the Lux Fridman podcast.", {'entities':[(64,71,'BOOK')]}),]

nlp = spacy.load("en_core_web_sm")

db = DocBin()

for text, annot in tqdm(TRAIN_DATA):
    doc = nlp.make_doc(text)
    ents = []
    for start, end, label in annot["entities"]:
        span = doc.char_span(start, end, label = label, alignment_mode= "contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents
    db.add(doc)
os.chdir('./src')
db.to_disk("./train.spacy")
