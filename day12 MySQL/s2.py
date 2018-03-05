#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql


conn = pymysql.connect(host='192.168.2.202', port=3306, user='root', passwd='123', db='q1day39')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# callproc执行存储过程，如果存储过程内部有SQL也会一并执行
row = cursor.callproc('proc_p1', (1, 2, 3))    # 如果存储过程中有out变量，直接忽略此处传参
# 获取存储过程中的select的查询结果（如果有查询操作）
selc = cursor.fetchall()
print(selc)


# 获取存储过程返回值
effect_row = cursor.execute('select @_proc_p1_0, @_proc_p1_1, @_proc_p1_2')  # 格式固定：_ + 存储过程名字 + _ + 参数索引（0表示获取存储过程第一个参数的值）
# 取存储过程返回值
result = cursor.fetchone()

print(result)
conn.commit()
cursor.close()
conn.close()




