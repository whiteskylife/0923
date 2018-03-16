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
    son = relationship('Son')


class Son(Base):
    __tablename__ = 'son'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    age = Column(String(16))

    father_id = Column(Integer, ForeignKey('father.id'))
    # father = relationship('Father')

    # __table_args__ = (
    #     UniqueConstraint('id', ' name', name='uix_id_name'),
    #     Index('ix_id_name', 'name', 'extra'),
    # )


# Base.metadata.create_all(engine)
Base.metadata.drop_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


f1 = Father(name='alvin', age=50)
session.add(f1)
session.commit()            # 此处不提交，后面报错无法建立外键约束

w1 = Son(name='little alvin1', age=4, father_id=1)
w2 = Son(name='little alvin2', age=5, father_id=1)

# f1.son = [w1, w2]

session.add_all([f1, w1, w2])
session.commit()

