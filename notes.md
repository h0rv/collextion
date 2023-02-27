# Project-related Notes

  Process Lex Fridman podcast transcripts (via Whisper: <https://karpathy.ai/lexicap/index.html>) to detect mentioned/recommended books via named entity recognition techniques. 

  Similar to <https://www.lexfridmanlibrary.com/>, but automated and actually maintainable 

  ```
  Lex Fridman Podcast (Source from YouTube) 
    ➙ OpenAI Whisper Speech-to-Text 
      ➙ Transcribed Podcast 
        ➙ Book Name Recognition Model 
          ➙ Book Recommendations for Given Podcast
            ➙ Display on web-app
  ```

## Data and APIs

  - Podcast:
    - YouTube: https://youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4
    - RSS feed for new posts: https://lexfridman.com/podcast/ 
  - Books:
    - https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks

## Tech Stack

  - NLP:
    - <https://github.com/explosion/spaCy> (Python)
  - Static site generators:
    - <https://www.11ty.dev/>
    - <https://gohugo.io/>

## Features

  1. Automatically update site when new podcasts release
  2. Who mentioned it? Lex or the guest? Might be nontrivial depending on the output of Whisper
  3. Show most mentioned books, and other metrics/statistics
  4. Cluster books by discipline (Computer Science, Physics, Biology, etc.)
  5. Can be done by book genre, or the discipline of the podcast guest

