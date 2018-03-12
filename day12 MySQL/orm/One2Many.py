#!/usr/bin/env python
# -*-coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:123@192.168.2.202:3306/com')

Base = declarative_base()


# 一对多，先创建两张表, 外键约束写在“多”的表中
class Men(Base):
    __tablename__ = 'men'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    age = Column(String(16))

    # __table_args__ = (
    # UniqueConstraint('id', 'name', name='uix_id_name'),
    #     Index('ix_id_name', 'name', 'extra'),
    # )

    def __repr__(self):
        return self.name


class Women(Base):
    __tablename__ ='women'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    age = Column(String(16))

    men_id = Column(Integer, ForeignKey('men.id'))
    # def __repr__(self):
    #     return self.age


Base.metadata.create_all(engine)

# Base.metadata.drop_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()
# select * from
# select id,name from women
# sql=session.query(Women).all()
# select * from women inner join men on women.men_id = men.id
# sql = session.query(Women.age,Men.name).join(Men).all()
# print(sql)
# print(sql)
# r = session.query(session.query(Women.name.label('t1'), Men.name.label('t2')).join(Men).all()).all()
# print(r)

# r = session.query(Women).all()
# print(r)


# m1=Men(name='alex',age=18)
# w1=Women(name='如花',age=40)
# w2=Women(name='铁锤',age=45)
# m1.gf=[Women(name='如花',age=40),Women(name='铁锤',age=45)]

# m1=Men(name='alex',age=18)
# w1=Women(name='如花',age=40,men_id = 1)
# w2=Women(name='铁锤',age=45,men_id = 1)
# session.add_all([w1,w2])
# session.commit()