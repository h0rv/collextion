FROM python:3.9 as backend

WORKDIR /app/src/
COPY /src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_lg

COPY /src/ .

FROM node:19 as frontend

# Copy the Python interpreter and libraries from the backend stage
COPY --from=backend /usr/local/bin/python /usr/local/bin/python
COPY --from=backend /usr/local/lib/python3.9 /usr/local/lib/python3.9
COPY --from=backend /usr/local/lib/libpython3.9.so.1.0 /usr/local/lib/

# Copy the src directory from the backend stage
COPY --from=backend /app/src/ /app/src/

WORKDIR /app/site/
COPY /site/package.json .

RUN npm install --global --quiet

COPY /site/ .

EXPOSE 8080

CMD python /app/src/model.py \
	npx @11ty/eleventy --serve --port=$PORT

