#!/bin/sh

mp3_url=$1
output=$2


curl -L $mp3_url -o $output
