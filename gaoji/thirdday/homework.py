#!/usr/bin/env python
#coding=utf-8
import urllib
import urllib2
import re

url1 = "http://www.douban.com/group/haixiuzu/"

req = urllib2.Request(url1)
response = urllib2.urlopen(req)
page = response.read()

page1 = re.compile(ur'\<a href="(http://www.douban.com/group/topic/.*?)"\stitle.*\sclass=""')
###u unicode   r  raw_str 后面的特殊符号不需要转义
matches = re.findall(page1,page)

img_list = []

for i in matches:
    try:
        req = urllib2.Request(i)
        response = urllib2.urlopen(req)
        page2 = reaponse.read()
        print page2
        p = re.compile(ur'<div class="topic-figure cc">\s*<img src="(.*?)" alt="" class="">\s*</div>')
        pmatches = re.findall(p,page2)
        print pmatches
        img_list.extend(pmatches)
    except:
        pass
print img_list        
