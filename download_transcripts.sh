#!/bin/sh

mkdir -p data/

if [ ! -f data/lexicap.zip ]; then
	# Zip doesn't exist; download it!
	curl -o data/lexicap.zip "https://karpathy.ai/lexicap/data.zip"
fi

unzip -j data/lexicap.zip vtt/*large.vtt -d data/lexicap

