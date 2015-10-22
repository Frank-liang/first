#!/usr/bin/env python
# coding : utf-8
import MySQLdb
db = MySQLdb.connect("127.0.0.1","root","zcool888","test")
cursor = db.cursor()
sql = "SELECT * FROM test"
try:
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" %(fname,lname,age,sex,income)
except:
    print "ERROR: Unable to fatch data"

db.close()
