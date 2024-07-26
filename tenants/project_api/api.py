from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Blueprint, render_template


project_api  = Blueprint('project_api',__name__,template_folder='templates',static_folder='static')
engine = create_engine(
    'postgresql://postgres:postgres@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session() 

@project_api.route('/home')
def home():
    return render_template('other/home.html')

@project_api.route('/menu')
def menu():
    return render_template('other/menu.html')

@project_api.route('/find_store')
def find_store():
    return render_template('other/find_store.html')

@project_api.route('/contect_us')
def contect_us():
    return render_template('other/contectus.html')
