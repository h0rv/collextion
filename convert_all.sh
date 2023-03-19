#!/bin/sh

vtt_dir="data/lexicap"
suffix="_large.vtt"

for f in "$vtt_dir"/*; do
	out=${f%"$suffix"}.txt
	./vtt2txt.sh "$f" "$out"
done

rm "$vtt_dir"/*.vtt

