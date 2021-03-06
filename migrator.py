#! /usr/bin/python

# Peter Novotnak :: Binarysprocket :: 2012

import oauth.oauth as oauth
import requests
import json

import difflib

from sys import stdout



#TODO
include = [
    'events',
    'todolists',
    'todos', ]



def get_project(site, username, password, company_id, project_name):
    site = 'basecamp.com'
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
        print "I found: \"", project_name[0], "\" :: I'm going forward with that."
        project_name = project_name[0]
    else:
        exit

    for p in r.json:
        if project_name == p['name']:
            return p



def get_users(site, username, password, company_id, project_json, topic_json, message_json):

    user_ids = []
    for t in topic_json :
        x = t['last_updater']['id']
        if not x in user_ids :
            user_ids.append(x)

    for m in message_json['messages'] :
        x = m['creator']['id']
        if not x in user_ids :
            user_ids.append(x)

    users = []
    for user in user_ids :
        url_dict = {
            'co_id' : company_id,
            'pr_id' : project_json['id'],
            'us_id' : user,
            }

        auth_en = requests.auth.HTTPBasicAuth
        url = "https://"+site+"/%(co_id)s/api/v1/people/%(us_id)s.json" % url_dict
        r = requests.get(url, auth=auth_en(username, password)).text
        users.append(r)

    return users



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



def get_todos(site, username, password, company_id, project_json, topic_json ):

    url_dict = {
        'co_id' : company_id,
        'pr_id' : project_json['id'], }

    auth_en = requests.auth.HTTPBasicAuth
    url = "http://"+site+"/%(co_id)s/api/v1/projects/%(pr_id)s/todolists.json" % url_dict
    in_progress = requests.get(url, auth=auth_en(username, password)).json
    completed = requests.get(url, auth=auth_en(username, password)).json

    return { 'active' : in_progress, 'completed' : completed }

def dummy():

    todos = []
    for topic in topic_json:
        if topic['topicable']['type'] == 'Todo':
            todos.append(topic)

    print todos
    for todo in todos:
        auth_en = requests.auth.HTTPBasicAuth
        url_dict = {
            'co_id' : company_id,
            'pr_id' : project_json['id'],
            'td_id' : 'a' }

        r = requests.get("http://"+site+"/%(co_id)s/api/v1/projects/%(pr_id)s/todos/%(td_id)s.json", auth=auth_en(username, password)).json
        messages.append(r)

        comments.append( requests.get(message['topicable']['url'], auth=auth_en(username, password)).json )

    return todos





################################################################




def put_messages(api_key, url, messages_and_comments):

    url = 'http://'+url+''
    #requests.get(url











