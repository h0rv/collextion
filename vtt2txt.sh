#!/bin/sh

input=$1
output=$2

if [[ -z "$input" || -z "$output" ]]; then
    echo "Not enough inputs"
    exit 1
fi

cat $input				\
	| grep : -v			\
	| awk '!seen[$0]++' \
	| tail -n +3		\
	> $output

