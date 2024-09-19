# All The Function Related to the Users it will be here

import uuid
import os
from werkzeug.utils import secure_filename
from flask import redirect, render_template, request, url_for
from common.database import db
from common.model import Users


def Signup_user():
    id = str(uuid.uuid4())
    name = request.form.get('name')
    dp_addr_file = request.files.get('dp_addr_file')
    email = request.form.get('email')
    phone = request.form.get('phone')
    password = request.form.get('password')
    filename = None
    if dp_addr_file:
        filename = secure_filename(dp_addr_file.filename)
        dp_addr_file.save(os.path.join('E:/vrushabh/College/Project/back_end/static/users_dp', filename))
            
    add_user = Users(id=id,name=name,dp_addr=filename,email=email,phone=phone,password=password,is_admin = False)
    db.session.add(add_user)
    db.session.commit()

def Login_user():
    email = request.form.get('email')
    password = request.form.get('password')
    user = Users.query.filter_by(email=email).first()
    if user:
        if user.password == password and user.email == email:
            user.is_active = True
            db.session.commit()
            return user
    return False

# Function for profile
def User_profile(uid):
    details = Users.query.filter_by(id=uid).first()
    if details:
        return details
    return False

def update(user):
    username = request.form.get('uname')
    phone = request.form.get('uphone')
    email = request.form.get('uemail')
    pswd = request.form.get('upswd')

    print("Old username: " + user.name)
    print("Old phone: " + user.phone)
    print("Old email: " + user.email)
    print("Old password: " + user.password)
    print("--------------------------------")
    print(f"New username: {username}")
    print(f"New phone: {phone}")
    print(f"New email: {email}")
    print(f"New password: {pswd}")

    user.name = username
    user.phone = phone
    user.email = email
    user.password = pswd
    try:
        db.session.commit()
        print("Update successful")
    except Exception as e:
        print(f"Error updating user: {e}")
        db.session.rollback() 