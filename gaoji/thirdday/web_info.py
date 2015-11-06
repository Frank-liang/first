#!/usr/bin/env python
#coding=utf-8

import urllib
import urllib2

url = 'http://www.zcool.com.cn'
req = urllib2.Request(url)
response = urllib2.urlopen(req)
print response.info()
print response.info().__class__

