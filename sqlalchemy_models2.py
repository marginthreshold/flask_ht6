from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class User2(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(3))
    lastname = Column(String(3))
    email = Column(String)
    birthdate = Column(Date)
    address = Column(String(5))
    orders = relationship("Orders", back_populates='user')


class Goods(Base):
    __tablename__ = 'goods'

    id = Column(Integer, primary_key=True)
    name = Column(String(3))
    description = Column(String(3))
    price = Column(Integer())
    orders = relationship("Orders", back_populates='goods')


class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User2", back_populates='orders')
    order_id = Column(Integer, ForeignKey('goods.id'))
    goods = relationship("Goods", back_populates='orders')
    date = Column(Date)
    status = Column(String(5))
