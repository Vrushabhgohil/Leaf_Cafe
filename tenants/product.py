import uuid
import os
from werkzeug.utils import secure_filename
from flask import request
from common.database import db
from common.model import *

def New_prduct():
    id = str(uuid.uuid4())
    name = request.form.get('name')
    img_addr_file = request.files.get('img_addr_file')
    price = request.form.get('price')
    qty = request.form.get('qty')
    desc = request.form.get('desc')
    ptype = request.form.get('ptype')
    filename = None
    if img_addr_file:
        filename = secure_filename(img_addr_file.filename)
        img_addr_file.save(os.path.join('E:/vrushabh/College/Project/back_end/static/users_dp', filename))
            
    add_product = Product(id=id,name=name,image_addr=filename,price=price,qty=qty,desc=desc,ptype=ptype,status="Publish")
    db.session.add(add_product)
    db.session.commit()

def updateProduct(product,id):
    name = request.form.get('name')
    img_addr_file = request.files.get('img_addr_file')
    price = request.form.get('price')
    qty = request.form.get('qty')
    desc = request.form.get('desc')
    ptype = request.form.get('ptype')
    if name:
        product.name = name
    if price:
        product.price = price
    if qty:
        product.qty = qty
    if desc:
        product.desc = desc
    if ptype:
        product.ptype = ptype
    db.session.commit()
    

def New_offer():
    id = str(uuid.uuid4())
    banner_img = request.files.get('banner_img')
    filename = None
    if banner_img:
        filename = secure_filename(banner_img.filename)
        banner_img.save(os.path.join('E:/vrushabh/College/Project/back_end/static/users_dp', filename))
            
    add_offer = Special(id=id,image_addr=filename)
    db.session.add(add_offer)
    db.session.commit()

def All_User():
    users = Users.query.filter_by(is_admin=False)
    return users

def All_Product():
    products = Product.query.filter_by(status="Publish")
    return products

def filter_user():
    user = Users.query.filter_by(is_admin=False).order_by(Users.created_at.desc()).limit(4)
    return user

def filter_product():
    product = Product.query.order_by(Product.added_at.desc()).limit(8)
    return product

def filter_Offers():
    product = Special.query.order_by(Special.added_at.desc()).limit(4)
    return product