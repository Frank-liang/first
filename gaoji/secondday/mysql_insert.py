#!/usr/bin/env python
#coding : utf-8

import MySQLdb

db = MySQLdb.connect("127.0.0.1","root","zcool888","test")
cursor = db.cursor()
sql = """INSERT INTO test(first_name,last_name,age,sex,income)
         VALUES ("p","l",30,"m",1)""" 
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()    
