#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine, and_, or_, func, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

# engine = create_engine('sqlite:///dbyuanabcd4970.db', echo=True)
engine = create_engine('mysql+pymysql://root:123456@192.168.1.110:3306/com?charset=utf8')  # 数据有中文要设置charset参数

Base = declarative_base()  # 生成一个SqlORM 基类


class HostToGroup(Base):
    __tablename__ = 'host_2_group'
    nid = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey("host.id"))
    group_id = Column(Integer, ForeignKey("group.id"))


class Host(Base):
    __tablename__ = 'host'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)
    ip_addr = Column(String(128), unique=True, nullable=False)
    port = Column(Integer, default=22)
    group = relationship('Group',
                         secondary=HostToGroup.__table__,
                         backref='host_list')

    # group =relationship("Group",back_populates='host_list')
    def __repr__(self):
        return "<id=%s,hostname=%s, ip_addr=%s>" % (self.id,
                                                    self.hostname,
                                                    self.ip_addr)


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)

    def __repr__(self):
        return "<id=%s,name=%s>" % (self.id, self.name)


Base.metadata.create_all(engine)  # 创建所有表结构

if __name__ == '__main__':
    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()

    # g1 = Group(name='g1')
    # g2 = Group(name='g2')
    # g3 = Group(name='g3')
    # g4 = Group(name='g4')
    # session.add_all([g1, g2, g3, g4])
    # h1 = Host(hostname='h1',ip_addr='192.168.1.56')
    # h2 = Host(hostname='h2',ip_addr='192.168.1.57',port=10000)
    # h3 = Host(hostname='ubuntu',ip_addr='192.168.1.58',port=10000)
    #
    # h1.group=[g2,g4]
    # session.add_all([h1, h2, h3])
    # session.commit()

    # h2主机绑定3个组
    # groups = session.query(Group).all()
    # h2 = session.query(Host).filter(Host.hostname=='h2').first()
    # h2.group = groups[:-1]                     # 从列表中取第一个到最后一个（不包含）元素, h2一台主机绑定3个组
    # # session.commit()
    # print(h2.group)
    # print("===========>", h2.group)



    g4 = session.query(Group).filter(Group.name=='g4').first()
    print(g4)
    obj1 = session.query(Host).filter(Host.hostname == 'h1').update({'port': 444})   # update 更新字段，必须用字典形式

    obj2 = session.query(Host).filter(Host.hostname == 'h1').first()

    # 关联g4和obj2
    # g4.host_list = [obj2, ]             # 从组的角度来做的；如果之前有绑定关系，此处用列表的append方法，否则会覆盖之前列表中的对象

    obj2.group = [g4, ]              # 第二种方式，从主机的角度来做
    session.commit()

# 小结: 增(插入数据):add/add_all方法; 删:  '改 update方法；查:query方法
# 一对一：外键是唯一的；不过一对一的关系完全可以放入一张表中，再建立一个字段即可，一对一很少用；实现：在一对多的foreignkey，后面加上unique=True


