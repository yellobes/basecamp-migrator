#! /bin/bash

#  Peter Novotnak, 2012 :: Binarysprocket LLC
#
#         http://binarysprocket.com
#


DIR="."
COOKIES="$DIR/cookies.txt"

USERNAME="peter@binarysprocket.com"
PASSWORD="ph171ps"
BASECAMP_ID=1761408

BASE_URL="https://basecamp.com/$BASECAMP_ID/api/v1"

URL_FEEDSTOCK="$1"





while read line
  do
    curl -k -u "$USERNAME:$PASSWORD" --cookie-jar "$COOKIES" "$BASE_URL/${line//1/1761408}" > "./data/${line//'/'/-}.json"
    sleep .05
  done <$URL_FEEDSTOCK




