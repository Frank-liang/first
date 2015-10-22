#!/usr/bin/env python
#coding : uft-8

import MySQLdb as MDB

db = MDB.connect("127.0.0.1","root","zcool888","test")
cursor = db.cursor()
cursor.execute("select VERSION()")
data = cursor.fetchone()
print "Database version is %s" %data
db.close()



