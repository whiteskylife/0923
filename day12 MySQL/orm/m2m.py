#!/usr/bin/env python
# -*-coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

# engine = create_engine('sqlite:///dbyuan674uu.db', echo=True)
engine = create_engine('mysql+pymysql://root:123456@192.168.1.110:3306/com?charset=utf8')  # 数据有中文要设置charset参数

Base = declarative_base()


class Men_to_Wemon(Base):             # 关系表一定放在最上面
    __tablename__ = 'men_to_wemon'
    nid = Column(Integer, primary_key=True)
    men_id = Column(Integer, ForeignKey('men.id'))
    women_id = Column(Integer, ForeignKey('women.id'))


class Men(Base):
    __tablename__ = 'men'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    age = Column(String(16))


class Women(Base):
    __tablename__ = 'women'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    age = Column(String(16))
    bf = relationship("Men", secondary=Men_to_Wemon.__table__, backref='gf')     # 进行关联查询之用，不会在表中生成字段

# 如果用到多对多的关系，而且用到了relationship，里面必须有一个属性secondary,secondary是和第三张关系表建立关联关系


Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# m1 = Men(name='alex', age=18)
# m2 = Men(name='wusir', age=18)
# w1 = Women(name='如花', age=40)
# w2 = Women(name='铁锤', age=45)
#
# session.add_all([m1, m2, w1, w2, ])
# session.commit()
#
# t1 = Men_to_Wemon(men_id=1, women_id=2)


m1 = session.query(Men).filter_by(id=2).first()     # 不加first取不到男人表中的对象，m1只能拿到SQL语句
w1 = session.query(Women).all()                     # 获取女人表所有对象
m1.gf = w1                                          # 根据 Women表中的relationship绑定关系：一个男人对应两个女人
session.add(m1)                                     # 把对应关系写入数据库的关系表（Men_to_Wemon）中，这里不会添加查询出的m1到man表

# m1.gf=[w1,w2]
# w1.bf=[m1,m2]
#
#
# session.add(t1)
session.commit()


# 小结：一对多是通过字段建立关联关系，  多对多用了relationship是通过对象的方式建立关联关系
