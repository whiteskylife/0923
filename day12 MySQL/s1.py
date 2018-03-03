#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql


# 创建连接
conn = pymysql.connect(host='192.168.2.202', port=3306, user='root', passwd='123', db='0227')
# 创建游标,默认元组类型，大元组套小元组
# cursor = conn.cursor()

# 创建游标,游标设置为字典类型（默认元组类型，大元组套小元组）
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update user set username='wahaha'")
# effect_row = cursor.execute("insert into user(username, password) values('pymysql','177')")

# 批量插入数据
# effect_row = cursor.executemany("insert into user(username, password) values(%s, %s)",
#                                 [("executemany_sql", "sql_1"), ("executemany_sql", "sql_2")])


# 获取查询数据
# fetchall 获取所有数据：
# effect_row = cursor.execute("select * from user")
# result = cursor.fetchall()
# print(result)

# fetchone
effect_row = cursor.execute("select * from user where nid > %s order by nid desc", (5,))
result = cursor.fetchall()          # 游标指针移动1
print(result)
result = cursor.fetchone()          # 获取指针移动1，排序后的第一条数据
print(result)
# 结果：
# {'username': 'executemany_sql', 'department': None, 'nid': 14, 'password': 'sql_2', 'email': None}
# {'username': 'executemany_sql', 'department': None, 'nid': 13, 'password': 'sql_1', 'email': None}

# fetchamany
# effect_row = cursor.execute("select * from user where nid > %s order by nid desc", (5,))
# result = cursor.fetchmany(3) # fetchmany（3）结果相当于三次fetchone
# print(result)
# 结果：[{'email': None, 'username': 'executemany_sql', 'nid': 14, 'password': 'sql_2', 'department': None},
# {'email': None, 'username': 'executemany_sql', 'nid': 13, 'password': 'sql_1', 'department': None},
# {'email': None, 'username': 'pymysql', 'nid': 12, 'password': '177', 'department': None}]

# scroll：移动指针
# relative
# effect_row = cursor.execute("select * from user where nid > %s order by nid desc", (5,))
# result = cursor.fetchone()
# print(result)
# result = cursor.fetchone()
# print(result)
# cursor.scroll(2, mode='relative')       # relative相对移动，从指针当前所在位置移动
# result = cursor.fetchone()
# print(result)
# 输出
# {'username': 'executemany_sql', 'nid': 14, 'department': None, 'password': 'sql_2', 'email': None}
# {'username': 'executemany_sql', 'nid': 13, 'department': None, 'password': 'sql_1', 'email': None}
# {'username': 'wahaha', 'nid': 10, 'department': 'CBA', 'password': '123', 'email': None}

# absolute
# effect_row = cursor.execute("select nid, username from user where nid > %s order by nid ", (0,))
# result = cursor.fetchone()
# print(result)
# result = cursor.fetchone()
# print(result)
# cursor.scroll(0, mode='absolute')       # absolute，0移动到开头位置
# result = cursor.fetchone()
# print(result)
# 输出
# {'nid': 1, 'username': 'wahaha'}
# {'nid': 2, 'username': 'wahaha'}
# {'nid': 1, 'username': 'wahaha'}

# lastrowid: 取自增id（最后一行）
# effect_row = cursor.executemany("insert into user(username, password) value(%s, %s)",
#                             [("aaa", "bbb"), ("yyy", "111")])
# conn.commit()   # 要先提交才能用lastrowid
# print(cursor.lastrowid)


# 提交，不然无法保存新建或者修改的数据,执行查询操作时无需执行commit
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()
