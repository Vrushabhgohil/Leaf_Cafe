from flask_login import current_user
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Blueprint, render_template


project_api  = Blueprint('project_api',__name__,template_folder='templates',static_folder='static')
engine = create_engine(
    'postgresql://postgres:postgres@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session() 

@project_api.route('/home/<string:tenant>')
def home(tenant):   
    return render_template('other/home.html',tenant=tenant)

@project_api.route('/menu/<string:tenant>')
def menu(tenant):
    return render_template('other/menu.html',tenant=tenant)

@project_api.route('/find_store/<string:tenant>')
def find_store(tenant):
    return render_template('other/find_store.html',tenant=tenant)

@project_api.route('/contect_us/<string:tenant>')
def contect_us(tenant):
    return render_template('other/contectus.html',tenant=tenant)
