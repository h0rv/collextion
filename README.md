# collextion

[![Netlify Status](https://api.netlify.com/api/v1/badges/4dbcbba8-8935-490e-8850-b228547bfc97/deploy-status)](https://app.netlify.com/sites/collextion/deploys)

A website to display book recommendations from the [Lex Fridman Podcast](https://lexfridman.com/podcast/).

Final project for CS 1699 Practical AI, Spring 2023.

## Install dependencies

  ```bash
  cd src/
  pip install -r requirements.txt
  python -m spacy download en_core_web_sm
  python -m spacy download en_core_web_lg
  ```

## Secrets

  ```bash
    cp src/example.env 
    cp src/.env 
  ```

  Fill in required secrets in `.env` file

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

## Running with Docker

  ```
  docker run --name site --rm -it $(docker build -q .)
  ```

---

## TODO

  - [ ] OpenAI Whisper integration
    - [ ] Add logic to be alerted of a new podcast post (likely from RSS feed)
  - [ ] Host on Google Cloud
    - [x] Create Dockerfile
    - [x] Automatic triggers and builds on pushes to main
    - [ ] Run container on GC
    - [ ] Run cron job to check for new podcast
  - [x] Remove duplicate posts
  - [ ] Increase model accuracy
    - [ ] Look into a case-_insensitve_ model that does not rely on capitalization (this is bottlenecked by Whisper)
    - [x] "Capitalization normalization" did not work
  - [ ] Categorizing recommendations
    - [ ] Add genre information to each book
    - [ ] Create running lists of reccomended books. This will include a "reccomended_in" with each podcast it was mentioned 
  - [x] Setup `env` for API keys

