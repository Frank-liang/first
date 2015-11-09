#!/usr/bin/env python
#coding=utf-8
import urllib2
from multiprocessing import Pool
urls = [
    'http://www.baidu.com/s?wd=reboot',
    'http://www.baidu.com/s?wd=reboot+python',
    'http://www.baidu.com/s?wd=reboot+devops',
    'http://www.baidu.com/s?wd=reboot+ops',
    'http://www.baidu.com/s?wd=reboot+gko_pool',
]
pool = Pool(4)

results = pool.map(urllib2.urlopen,urls)
pool.close()
pool.join()
