#!/usr/bin/env python
# -*-coding:utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
print(sqlalchemy.__version__)

# 连接数据库，指定用哪个插件
# engine = create_engine('mysql+pymysql://root:123@192.168.2.202:3306/com', echo=True)    # echo:把由类翻译好的SQL打印出来
engine = create_engine('mysql+pymysql://root:123456@192.168.1.110:3306/com')    # echo:把由类翻译好的SQL打印出来

Base = declarative_base()   # 生成一个SQLORM基类


class User(Base):
    __tablename__ = 'users'   # 定义一个表名

    id = Column(Integer, primary_key=True, autoincrement=True)  # 主键特点：非空且唯一
    name = Column(String(40), index=True)                       # 要指定数据长度， index普通索引
    fullname = Column(String(40), unique=True)                  # unique唯一索引
    password = Column(String(40))

    def __repr__(self):
        """
        :return:返回对象具体值而非对象的内存地址
        """
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                            self.name, self.fullname, self.password)


# 建表
Base.metadata.create_all(engine)  # 调用子类中的字段创建所有表结构
# Base.metadata.drop_all(engine)  # 删除


# 创建session对象，准备插入数据（查询、插入数据前要创建session），这两行触发sessionmaker类下的__call__方法，return得到 Session实例，赋给变量session，所以session可以调用Session类下的add，add_all等方法
MySession = sessionmaker(bind=engine)
session = MySession()


# ed_user = User(name='xiaoyu', fullname='Xiaoyu Liu', password='123')  # 创建一个对象,包含了要插入的数据
# session.add(ed_user)  # 向数据库中插入数据
# our_user = session.query(User).filter_by(name='ed').first()  # SELECT * FROM users WHERE name="ed" LIMIT 1;

# session.add_all([                       # 插入多条数据
#     User(name='alex', fullname='Alex Li', password='456'),
#     User(name='alex', fullname='Alex old', password='789'),
#     User(name='peiqi', fullname='Peiqi Wu', password='sxsxsx')])
#
# session.commit()    # 提交到数据库

#print(">>>",session.query(User).filter_by(name='ed').first())

# all方法查询所有
print(session.query(User).all())  # （获取到一个包含所有对象的列表，每个对象中包含SQL查询的数据）打印表中的所有内容，User类中的 __repr__ 方法中把对象的值返回，才能打印出值而非对象的内存地址
for row in session.query(User).order_by(User.id):
    print(row)

# for row in session.query(User).filter(User.name.in_(['alex', 'wendy', 'jack'])):＃这里的名字是完全匹配
#     print(row)
# for row in session.query(User).filter(~User.name.in_(['ed', 'wendy', 'jack'])):  # ~User 取反name不在列表中的拿出来
#     print(row)
# print(session.query(User).filter(User.name == 'ed').count())




# 与和或的关系查询
# from sqlalchemy import and_, or_
# for row in session.query(User).filter(and_(User.name == 'ed', User.fullname == 'Ed Jones')):
#     print(row)
# for row in session.query(User).filter(or_(User.name == 'ed', User.name == 'wendy')):
#     print(row)
