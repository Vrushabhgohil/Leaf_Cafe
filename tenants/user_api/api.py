from flask_login import current_user, login_required
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Blueprint, redirect, render_template, request, url_for
from tenants.users import *


user_api  = Blueprint('user_api',__name__,template_folder='templates',static_folder='static')
engine = create_engine(
    'postgresql://postgres:postgres@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session() 

@user_api.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        Login_user()
        if Login_user():
            return redirect(url_for('user_api.home'))
        else:
            msg = "invalid email or password!!"    
            return render_template('user/login.html',msg=msg)
        
    return render_template('user/login.html')

@user_api.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        Signup_user()
        return redirect(url_for('user_api.login'))
    return render_template('user/signup.html')

@user_api.route('/profile')
def profile():
    one_user = User.query.filter_by(name='sam').first()
    return render_template('user/profile.html',one_user=one_user)

@user_api.route('/logout')
def logout():
    return "This is logout api"