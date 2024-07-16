# All The Function Related to the User it will be here

import uuid
import os
from werkzeug.utils import secure_filename
from flask import redirect, render_template, request, url_for
from common.database import db
from common.model import User


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
        dp_addr_file.save(os.path.join('E:\\vrushabh\\Project\back_end\static\\users_image',filename))

    add_user = User(id=id,name=name,dp_addr=filename,email=email,phone=phone,password=password)
    db.session.add(add_user)
    db.session.commit()

def Login_user():
    email = request.form.get('email')
    password = request.form.get('password')    

    user = User.query.filter_by(email=email).first()
    if user:
        if user.password == password and user.email == email:
            user.is_active = True
            db.session.commit()
            return True
    return False