#! /bin/bash

#  Peter Novotnak, 2012 :: Binarysprocket LLC
#
#         http://binarysprocket.com
#


DIR="."
COOKIES="$DIR/cookies.txt"
BASECAMP_ID=1761408
BASE_URL="https://basecamp.com/$BASECAMP_ID/api/v1"
USERNAME="peter@binarysprocket.com"
PASSWORD="ph171ps"


while read line
  do
    echo curl -k -u "$USERNAME:$PASSWORD" --cookie-jar "$COOKIES" "$BASE_URL/${line//1/1761408} >./data/${line//'/'/-}.json"
    sleep .05
  done <"./basecamp.href"




