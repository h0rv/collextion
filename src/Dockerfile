FROM python:3.9

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm
RUN python -m spacy download en_core_web_lg

COPY . .

CMD [ "python", "model.py" ]

