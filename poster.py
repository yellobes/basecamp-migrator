#! /usr/bin/python2.7


import urllib, urllib2


class Poster():
    
    def __init__(self):
        self.url = ''
        self.values = {}

    def load(self, url, values):
        if ( type({}) == type(values) ) & ( type('') == type(url) ):
            self.url = url
            self.values = values
        else :
            raise TypeError("url or values is wrong type [string, dict]")
        self.data = urllib.urlencode(values)

    def post(self):
        req = urllib2.Request(self.url, self.data)
        try:
            response = urllib2.urlopen(req)
        except ValueError:
            raise ValueError("Error! Did you specify protocol when you ran Poster.load(...)?")
        print response.info()
         
        



