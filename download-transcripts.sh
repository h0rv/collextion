#!/bin/sh

mkdir -p data/

curl -o data/lexicap.zip "https://karpathy.ai/lexicap/data.zip"

unzip -j data/lexicap.zip vtt/*large.vtt -d data/lexicap
