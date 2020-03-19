#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:34:20 2020

@author: meharsingh
"""




import tweepy 
import json



consumer_key = 'oOF0mw2kRLj6HZE6R9xKyqk3F'
consumer_secret = '0kNy058bq3dcjzDODjkHRKab6sLWX0a4YD4wdbNTDtwHRknTos'
access_key = '1224402602995212289-4TIUvRehKNY9vCNWz8ibZlILSNK87j'
access_secret = '5cHnNDnb4HHIGM3pV4neDemZQUJKncQ0e4QCejziqchko'


#print(api)
def searching(query):
    from googlesearch import search
    for link in search(query, tld="com", num=1, stop=1, pause=2):
        return link

# Authorization to consumer key and consumer secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

# Access to user's access key and access secret 
auth.set_access_token(access_key, access_secret) 

# Calling api 
api = tweepy.API(auth) 
#print(api)

#Will get trending topics in world
res = api.trends_place(1)

l_trends = json.loads(json.dumps(res, indent=1))
#print(l_trends[0]['trends'])

trending = []

for t in l_trends[0]['trends']:
    trending.append(t['name'].replace('#',''))

selected = []

# this will select top 10 trends
top_links = []

for i in range(0,10):
    links = []
    links = searching(trending[i])
    top_links.append("The trending topic: "+str(trending[i]) + "The links: " + str(links))
for i in range(0,10):
    print('\n'+top_links[i])







