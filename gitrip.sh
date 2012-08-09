#! /bin/bash


WAIT=2
TMP_FILE='./basecamp.href'





while read line
  do
    continue
    curl -sk "$line" | awk '/json/&&/GET/' | awk -F'GET' '{print $2}' | awk -F'</code>' '{print $1}' >> "$TMP_FILE"

    # Dont DoS github!
    echo "
    
    Waiting $WAIT seconds...
    
    "
    for (( i = $WAIT; i >= 1; i-- ))
    do
    echo -ne "$i"
      for x in {1..4}
      do
        sleep .25
        echo -ne '.'
       done
     echo ''
    done
   echo '
   '
   done <"./sections.href"

sed -i 's/ //g;s/^\///g' "$TMP_FILE"

