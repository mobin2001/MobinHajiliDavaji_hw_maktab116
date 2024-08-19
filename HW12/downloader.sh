#!/bin/bash
read -p "paste downlad link here: " link

if [ -z "$link" ]; then
    echo "usage: $0 <URL>"
    exit 1
fi

URL=$link
echo "$(date): Download $URL" >> log.txt

wget $URL
exit 0
