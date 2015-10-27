#!/usr/bin/env python
#coding=utf-8

import urllib
import urllib2

data = {}
data['name'] = 'pc'
data["location"] = 'zcoo'
data['language'] = 'py'
url_values = urllib.urlencode(data)
print url_values

url = 'http://127.0.0.1:8888'
full_url = url + '?' + url_values
data =urllib2.urlopen(full_url)
