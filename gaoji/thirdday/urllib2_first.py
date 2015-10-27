#!/usr/bin/env python
#coding=utf-8

import urllib2
response = urllib2.urlopen('http://51reboot.com/')
html = response.read()
print html
