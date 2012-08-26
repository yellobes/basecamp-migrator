#! /usr/bin/python2.7


# Parses messages (index.html) and ejects content in csv format

# REQUIRES :: Beautiful Soup 4 :: pip install beautifulsoup | apt-get install python-beautifulsoup



from bs4 import BeautifulSoup
import fileinput





def parse_index() :

    # Assemble the soup from stdin / file
    html = ''
    for line in fileinput.input() :
        html += line
    soup = BeautifulSoup(html)
    trs = soup.find_all('tr')

    # Suss out the values
    x = 0
    i = 0
    author = ''
    link_href = ''
    link_text = ''
    description = ''
    date = ''
    num_comments = ''

    message = []
    for tr in trs :
        tds = tr.find_all('td')
        for td in tds :
            if i == 0 :
                author = td.get_text()
            elif i == 1 :
                link_href = td.a.get('href')
                link_text = td.a.get_text()
                description = td.get_text()
            elif i == 2 :
                date = td.get_text()
            elif i == 3 :
                num_comments =  str(td.get_text()).split()[0]

            i = i + 1
        
        message = {
            'author' : author,
            'link_href' : link_href,
            'link_text' : link_text,
            'description' : description,
            'date' : date,
            'num_comments' : num_comments,
        }
        


def return_results() :
    message_set = parse_index()
    print type(message_set)





return_results()




