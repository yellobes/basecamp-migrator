#! /usr/bin/python2.7


# Parses topics (index.html) and 

# REQUIRES :: Beautiful Soup 4 :: pip install beautifulsoup | apt-get install python-beautifulsoup



from bs4    import BeautifulSoup
from os     import system
from time   import clock

from poster import Poster as p

import sys
import fileinput
import cgi

project_id = sys.argv[1]
ac_url = sys.argv[2]
ac_api_token = sys.argv[3]

p = P()

def post_topic(data) :
    for topic in topics :
        p.load(ac_url, data)
        p.post()


# Start the stopwatch
start = clock()
# Assemble the soup
html = ''

for line in sys.stdin :
    html += line
soup = BeautifulSoup(html)

tds = soup.find_all('td')

i = 1
x = 0
topics = []
for td in tds :
    if i == 1 :
        author = td.get_text()
    if i == 2 :
        title = td.a.get_text()
        description = td.get_text()
    if i == 3 :
        date = td.get_text()
    if i == 4 :
        num_comments = str( td.get_text() ).split(' ')[0]
        try :
            comments_link = td.a.get('href')
        except AttributeError :
            comments_link = None
        # Reset the array and add the values to the topics dict.
        i = 0
        topics.append({
            'author' : author,
            'title' : title,
            'description' : description,
            'date' : date,
            'num_comments' : num_comments,
            'comments_link' : comments_link,
        })
    i = i + 1

print "Parsed topics in ", (clock() - start), " seconds."

    


