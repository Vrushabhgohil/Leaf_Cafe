from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Blueprint, redirect, render_template, request, url_for
from tenants.users import *


user_api  = Blueprint('user_api',__name__,template_folder='templates',static_folder='static')
load_dotenv()
database_uri = os.getenv('DATABASE_URI')
engine = create_engine(database_uri)
Session = sessionmaker(bind=engine)
session = Session() 

@user_api.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = Login_user()
        breakpoint
        if user and user.is_admin == True:
            return redirect(url_for('admin_api.home', tenant=user.id))
        elif user and user.is_admin == False:
            return redirect(url_for('project_api.home', tenant=user.id))
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

@user_api.route('/profile/<string:tenant>')
def profile(tenant):
    user = User_profile(tenant)
    if user:
        return render_template('user/profile.html',tenant=tenant,user=user)
    return "No Data available"

@user_api.route('/update_profile/<string:tenant>',methods=['GET','POST'])
def update_profile(tenant):
    user = Users.query.get(tenant)
    if user:
        update(user)
        return redirect(url_for('user_api.profile',tenant=tenant))
    msg="User's details is not Update"
    return render_template('user/profile.html',tenant=tenant,msg=msg)



@user_api.route('/logout/<string:tenant>')
def logout(tenant):
    return "This is logout api"


    