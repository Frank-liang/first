#!/usr/bin/env python
import urllib
import urllib2
url = 'http://weibo.com/u/auxten'
req = urllib2.Request(url)
response = urllib2.urlopen(req)

print "URL",url
print response.geturl()
