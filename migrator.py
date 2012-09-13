#! /usr/bin/python

# Peter Novotnak :: Binarysprocket :: 2012

import oauth.oauth as oauth
import requests
import json

import difflib


# Our interface classes
class bc_JSON :
    
    username = ''
    password = ''

    def authenticate():
        pass

    def get_comments():
        pass
    def get_messages():
        pass
    def get_people():
        pass
    def get_todolists():
        pass
    def get_todos():
        pass

    def get_events():
        pass

def get_projects(username, password, company_id, project_name):
    url_dict = {
        'co_id' : company_id, }
    include = [
        'comments',
        'events',
        'messages',
        'people',
        'todolists',
        'todos', ]
    auth_en = requests.auth.HTTPBasicAuth
    url = "https://basecamp.com/%(co_id)s/api/v1/projects.json" % url_dict 
    r = requests.get(url, auth=auth_en(username, password))
    project_names = []
    for project in r.json:
        project_names.append(project['name'])

    project_name = difflib.get_close_matches(project_name, project_names, 1)

    if len(project_name) == 0:
        print "I couldn't find projects under the name you specified."
        exit
    elif len(project_name) > 1:
        print "I got: ", project_name, " You are going to have to narrow it down a bit."
        # TODO write a piece that allows the user to choose between the potential names.
        exit
    elif len(project_name) == 1:
        print "I found: ", project_name[0], " :: I'm going forward with that."
        project_name = project_name[0]
    else:
        exit
    
    for p in r.json:
        if project_name == p['name']:
            return p

def get_topics(username, password, company_id, project_json):
    class project_obj:
        id = str(project_json['id'])
    
    project = project_obj()

    url_dict = {
        'co_id' : company_id,
        'pr_id' : project.id,
        }

    auth_en = requests.auth.HTTPBasicAuth
    url = "https://basecamp.com/%(co_id)s/api/v1/projects/%(pr_id)s/topics.json" % url_dict 
    return requests.get(url, auth=auth_en(username, password)).json


 

def get_messages(username, password, company_id, project_json, topic_json):
    url_dict = {
        'co_id' : company_id,
        'pr_id' : project_json['id'],
        }

    message_identifiers = []
    for topic in topic_json:
        if topic['topicable']['type'] == 'Message':
            message_identifiers.append(topic)

    messages = []
    for message in message_identifiers:
        auth_en = requests.auth.HTTPBasicAuth
        messages.append(requests.get(message['topicable']['url'], auth=auth_en(username, password)).json)

    return messages

    #auth_en = requests.auth.HTTPBasicAuth
    #url = "https://basecamp.com/%(co_id)s/api/v1/projects/%(pr_id)s/messages/%(ms_id)s.json" % url_dict 
    #r = requests.get(url, auth=auth_en(username, password))

        

class ac_ :
    pass



# Transform input to orderd data ready for output
class Mapping :
    pass

# This class walks the topics / 
class Walker :
    pass




# example client using httplib with headers
#class SimpleOAuthClient(oauth.OAuthClient):
#
#    def __init__(self, server, port=httplib.HTTP_PORT, request_token_url='', access_token_url='', authorization_url=''):
#        self.server = server
#        self.port = port
#        self.request_token_url = request_token_url
#        self.access_token_url = access_token_url
#        self.authorization_url = authorization_url
#        self.connection = httplib.HTTPConnection("%s:%d" % (self.server, self.port))
#
#    def fetch_request_token(self, oauth_request):
#        # via headers
#        # -> OAuthToken
#        self.connection.request(oauth_request.http_method, self.request_token_url, headers=oauth_request.to_header()) 
#        response = self.connection.getresponse()
#        return oauth.OAuthToken.from_string(response.read())
#
#    def fetch_access_token(self, oauth_request):
#        # via headers
#        # -> OAuthToken
#        self.connection.request(oauth_request.http_method, self.access_token_url, headers=oauth_request.to_header()) 
#        response = self.connection.getresponse()
#        return oauth.OAuthToken.from_string(response.read())
#
#    def authorize_token(self, oauth_request):
#        # via url
#        # -> typically just some okay response
#        self.connection.request(oauth_request.http_method, oauth_request.to_url()) 
#        response = self.connection.getresponse()
#        return response.read()
#
#    def access_resource(self, oauth_request):
#        # via post body
#        # -> some protected resources
#        headers = {'Content-Type' :'application/x-www-form-urlencoded'}
#        self.connection.request('POST', RESOURCE_URL, body=oauth_request.to_postdata(), headers=headers)
#        response = self.connection.getresponse()
################        return response.read()