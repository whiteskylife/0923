#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql


conn = pymysql.connect(host='192.168.2.202', port=3306, user='root', passwd='123', db='q1day39')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

row = cursor.callproc('proc_sql', ('select * from man where nid > ?', 11))
result = cursor.fetchall()
print(result)
conn.commit()
cursor.close()
conn.close()




