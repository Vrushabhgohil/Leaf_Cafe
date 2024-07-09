from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Blueprint, render_template


user_api  = Blueprint('user_api',__name__,template_folder='templates',static_folder='static')
engine = create_engine(
    'postgresql://postgres:postgres@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session() 

@user_api.route('/login')
def login():
    return render_template('user/login.html')

@user_api.route('/signup')
def signup():
    return render_template('user/signup.html')

@user_api.route('/home')
def home():
    return render_template('projects/home.html')

@user_api.route('/logout')
def logout():
    return "This is logout api"