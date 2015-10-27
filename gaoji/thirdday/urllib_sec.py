#!/usr/bin/env python
#coding=utf-8
import urllib
import urllib2

url = 'http://127.0.0.1:8888'
user_agent = 'THIS IS A FALSE AGENT'
values = {'name':'lp','location':'zcool','language':'python'
      }   
headers = {'User-Agent': user_agent}    
data = urllib.urlencode(values)
rep = urllib2.Request(url,data,headers)
response = urllib2.urlopen(rep)
the_page = response.read()










