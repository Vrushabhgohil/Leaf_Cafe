import os
from dotenv import load_dotenv
from flask_login import current_user
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Blueprint, render_template
from tenants.product import *

project_api  = Blueprint('project_api',__name__,template_folder='templates',static_folder='static')
load_dotenv()
database_uri = os.getenv('DATABASE_URI')
engine = create_engine(database_uri)
Session = sessionmaker(bind=engine)
session = Session() 

@project_api.route('/home/<string:tenant>')
def home(tenant):   
    product = filter_product()
    offers = filter_Offers()
    return render_template('other/home.html',tenant=tenant,product=product,offers=offers)

@project_api.route('/menu/<string:tenant>')
def menu(tenant):
    product = filter_product()
    return render_template('other/menu.html',tenant=tenant,product=product)

@project_api.route('/find_store/<string:tenant>')
def find_store(tenant):
    return render_template('other/find_store.html',tenant=tenant)

@project_api.route('/contect_us/<string:tenant>')
def contect_us(tenant):
    return render_template('other/contectus.html',tenant=tenant)
