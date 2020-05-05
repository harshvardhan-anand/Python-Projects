#!/usr/bin/env python
# coding: utf-8

# In[174]:


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier


# class covid():
#     def __init__(self):
#         

# In[175]:


# https://stackoverflow.com/questions/13303449/urllib2-httperror-http-error-403-forbidden
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
req = Request("https://www.worldometers.info/coronavirus/country/india/", headers=hdr) # without user-agent we will get HTTP error
html = urlopen(req)
html


# In[176]:


obj = bs(html, features="lxml")


# In[177]:


list(obj.find("span", {"id":"updates"}).next_siblings)


# In[178]:


new_cases = obj.find("li",{"class":"news_li"}).strong.text.split()[0]  #new cases
obj.find("li",{"class":"news_li"}).strong.text.split()[0]


# In[179]:


death = (list(obj.find("li", {"class":"news_li"}).strong.next_siblings)[1]).text.split()[0]  #death
(list(obj.find("li", {"class":"news_li"}).strong.next_siblings)[1]).text.split()[0]


# In[180]:


notifier = ToastNotifier()


# In[181]:


message = "New Cases - "+new_cases+"\nDeath - "+death
notifier.show_toast(title="COVID-19 Updates", msg=message, duration=5, icon_path=r"virus.ico")

