#!/usr/bin/env python
#coding: utf-8

import MySQLdb

db = MySQLdb.connect("127.0.0.1","root","zcool888","test")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS test")
sql = """CREATE TABLE test (
       first_name CHAR(20) NOT NULL,
       last_name CHAR(20),
       age INT,
       sex CHAR(1),
       income FLOAT)"""
cursor.execute(sql)
db.close()

