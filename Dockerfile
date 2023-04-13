FROM python:3.9 as backend

WORKDIR /app/src/
COPY /src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_lg

COPY /src/ .

WORKDIR /app/
COPY download_transcripts.sh .
COPY vtt2txt.sh .
COPY convert_all.sh .

RUN bash download_transcripts.sh
RUN bash download_transcripts.sh
RUN bash convert_all.sh

FROM node:latest as frontend

# Copy the Python interpreter and libraries from the backend stage
COPY --from=backend /usr/local/bin/python /usr/local/bin/python
COPY --from=backend /usr/local/lib/python3.9 /usr/local/lib/python3.9
COPY --from=backend /usr/local/lib/libpython3.9.so.1.0 /usr/local/lib/

# Copy the src directory from the backend stage
COPY --from=backend /app/src/ /app/src/
COPY --from=backend /app/data/ /app/data/

COPY /schema/ /app/schema/

WORKDIR /app/site/
COPY /site/package.json .

RUN npm install --quiet

COPY /site/ .

EXPOSE 8080
EXPOSE $PORT

CMD python /app/src/main.py

