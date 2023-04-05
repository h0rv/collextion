# collextion

A website to display book recommendations from the [Lex Fridman Podcast](https://lexfridman.com/podcast/).

Final project for CS 1699 Practical AI, Spring 2023.

## Install dependencies

  ```bash
  pip install -r requirements.txt
  python -m spacy download en_core_web_sm
  python -m spacy download en_core_web_lg
  ```

## Download Pre-transcribed Transcripts

  ```bash
  ./download_transcripts.sh
  # Conver data to text format (removing timing informatio from *.vtt file)
  ./convert_all.sh
  ```

## Running the Backend

  ```bash
  cd src/
  ./main.py
  ```

## Running the site

  ```bash
  npm install --prefix site/
  npm start   --prefix site/
  ``` 

---

## TODO

  - [ ] OpenAI Whisper integration
    - [ ] Add logic to be alerted of a new podcast post (likely from RSS feed)
  - [ ] Host on Google Cloud
  - [ ] Remove duplicate posts
  - [ ] Increase model accuracy
    - [ ] Look into a case-_insensitve_ model that does not rely on capitalization (this is bottlenecked by Whisper)
  - [ ] Categorizing recommendations
    - [ ] Add genre information to each book
    - [ ] Create running lists of reccomended books. This will include a "reccomended_in" with each podcast it was mentioned 
  - [ ] Setup `env` for API keys

