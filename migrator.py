#! /usr/bin/python

# Peter Novotnak :: Binarysprocket :: 2012

import oauth.oauth as oauth
import requests
import json

import difflib

from sys import stdout




include = [
    'comments',
    'events',
    'messages',
    'people',
    'todolists',
    'todos', ]



def get_projects(site, username, password, company_id, project_name):
    url_dict = {
        'co_id' : company_id, }
    auth_en = requests.auth.HTTPBasicAuth
    url = "https://"+site+"/%(co_id)s/api/v1/projects.json" % url_dict 
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
        # TODO write a piece that allows the user to choose between the potential names,
        # then change the difflib.get_close_matches call, to allow more than one result.
        exit
    elif len(project_name) == 1:
        print "I found: ", project_name[0], " :: I'm going forward with that."
        project_name = project_name[0]
    else:
        exit
    
    for p in r.json:
        if project_name == p['name']:
            return p


def get_users(site, username, password, company_id, project_json):
    
    url_dict = {
        'co_id' : company_id,
        'pr_id' : project_json['id'],
        }

    auth_en = requests.auth.HTTPBasicAuth
    url = "https://"+site+"/%(co_id)s/api/v1/projects/%(pr_id)s/people.json" % url_dict 
    return requests.get(url, auth=auth_en(username, password)).text


def get_topics(site, username, password, company_id, project_json):

    url_dict = {
        'co_id' : company_id,
        'pr_id' : project_json['id'],
        }

    auth_en = requests.auth.HTTPBasicAuth
    url = "https://"+site+"/%(co_id)s/api/v1/projects/%(pr_id)s/topics.json" % url_dict 
    return requests.get(url, auth=auth_en(username, password)).json


 

def get_messages(site, username, password, company_id, project_json, topic_json):
    message_identifiers = []
    for topic in topic_json:
        if topic['topicable']['type'] == 'Message':
            message_identifiers.append(topic)


    messages = []
    comments = []
    for message in message_identifiers:
        auth_en = requests.auth.HTTPBasicAuth
        r = requests.get(message['topicable']['url'], auth=auth_en(username, password)).json
        messages.append(r)
        url_dict = {
            'co_id' : company_id,
            'pr_id' : project_json['id'],
            'ms_id' : message['id'] } 
        url = "https://"+site+"/%(co_id)s/api/v1/projects/%(pr_id)s/messages/%(ms_id)s/comments.json" % url_dict 
        comments.append( requests.get(message['topicable']['url'], auth=auth_en(username, password)).json )
        

    return { 'messages' : messages, 'comments' : comments }



def put_messages(api_key, url, messages_and_comments):
       
    url = 'http://'+url+''
    #requests.get(url
        










