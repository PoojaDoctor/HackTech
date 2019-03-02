#!/usr/bin/env python
# coding: utf-8

# In[100]:


import tweepy
from bs4 import BeautifulSoup as bs
import urllib
import requests
import regex as re
import pandas as pd


# In[95]:


req= requests.get('http://ip-api.com/json')

res = req.json()
latitude = res['lat']
longitude = res['lon']


# In[9]:


auth = tweepy.OAuthHandler("pFduB9dBKq5zvEWrAkhfTSnyv", "cBcMj9z9jIO3HhmeaykDdfaCsByDqQujF4mZ6VO8mTyjDn5SGG")
auth.set_access_token("1058601288223514624-piQQ1twMDAwuAg7jTwJzvjHIRGVGNA", "nOcTYajRX8RRQDQ5cb4Rpl12GVGM2atSUqpRRg2aCDP8n")

api = tweepy.API(auth)


# In[117]:


def get_trending_data(latitude, longitude, api):
    location = api.trends_closest(latitude, longitude)
    woeid = re.search(r'[^/]+$', location[0]['url'])
    woeid_fin = woeid.group(0)
    get_trends = api.trends_place(woeid_fin)
    return get_trends


# In[118]:


get_trending_data(latitude, longitude, api)


# In[ ]:




