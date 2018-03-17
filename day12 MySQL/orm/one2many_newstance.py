#!/usr/bin/env python
# -*-coding:utf-8 -*-
# !/usr/bin/env python
# -*- coding:utf-8 -*-


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

# engine = create_engine('sqlite:///dbyuan691.db', echo=True)
engine = create_engine('mysql+pymysql://root:123456@192.168.1.110:3306/com')

Base = declarative_base()


class Father(Base):
    __tablename__ = 'father'

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    age = Column(String(16))
    son = relationship('Son')       # son字段不会在表中生成，只是一个关系字段
    # son = relationship('Son', backref='father')      # backref:相当于在Son中定义father = relationship('Father')

    # def __repr__(self):
    #     return "name is %s, age is %s" % (self.name, self.age)


class Son(Base):
    __tablename__ = 'son'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    age = Column(String(16))

    father_id = Column(Integer, ForeignKey('father.id'))  # relationship底层根据ForeignKey来实现的
    father = relationship('Father')

    # __table_args__ = (
    #     UniqueConstraint('id', ' name', name='uix_id_name'),
    #     Index('ix_id_name', 'name', 'extra'),
    # )


Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ret = session.query(Father).filter_by(id=1)
# print(ret)
# ---------filter和filter by的区别：-------------
# 键值对儿的方式过滤用filter by
# 条件判断，条件过滤用filter

# first返回一个对象，如果Father类中没有__repr__方法，则可以用ret.name方式取对象对应的值
# ret = session.query(Father).filter_by(id=1).first()
# print(ret.name)
# print(ret.son)      # 和Father绑定的两个son对象，返回一个列表包含两个son对象
# for i in ret.son:
#     print(i.name)

# s1 = session.query(Son).filter_by(id=2).first()     # s1 返回一个过滤之后的儿子对象
# print(s1.father.name, s1.father.age, s1.father.id)  # 调用Son中的relationship(内部用的join...on内部做了封装),因为是一对多的关系，不需要加索引（列表中的索引）




# f1 = Father(name='alvin', age=50)
# session.add(f1)
# session.commit()            # 此处不提交，后面报错无法建立外键约束
#
# w1 = Son(name='little alvin1', age=4, father_id=1)
# w2 = Son(name='little alvin2', age=5, father_id=1)
#

f1 = session.query(Father).filter_by(id=1).first()
w3 = Son(name='little alvin6', age=5)
print(f1.son)
f1.son.append(w3)
print(f1.son)
session.add(f1)
session.commit()



# # f1.son = [w1, w2]
#
# session.add_all([f1, w1, w2])
# session.commit()

