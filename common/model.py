from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import Boolean, Column, DateTime, ForeignKey,Integer, String,ARRAY
from common.database import db

class Users(UserMixin, db.Model):
    __tablename__ = 'Users'
    __table_args__ = {'schema': 'myschema'}
    id = Column(String(100), primary_key=True)
    name = Column(String(250), nullable=False)
    dp_addr = Column(String(250),nullable=False,default='dummy-profile-pic-male1.jpg')
    email = Column(String(50), unique=True, nullable=False)
    phone = Column(String(10), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=None)
    is_active = Column(Boolean, default=True)


class Product(db.Model):
    __tablename__ = 'Product'
    __table_args__ = {'schema': 'myschema'}
    id = Column(String(100), primary_key=True)
    name = Column(String(250), nullable=False)
    image_addr = Column(String(250),nullable=False,default='unknown_product.png')
    price = Column(Integer,nullable=False)
    qty = Column(Integer,nullable=False)
    desc = Column(String(250),nullable=False)
    added_at = Column(DateTime, default=datetime.now, nullable=False)
    status = Column(String(35))

class Purchase(db.Model):
    __tablename__ = 'Purchase'
    __table_args__ = {'schema': 'myschema'}
    id = Column(String(100),primary_key=True)
    username = Column(String(50))
    products = Column(ARRAY(String(50)),nullable=False)
    prices = Column(ARRAY(Integer),nullable=False)
    total_price = Column(Integer,nullable=False)
    order_at = Column(DateTime, default=datetime.now, nullable=False)
    