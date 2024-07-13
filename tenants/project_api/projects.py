from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Blueprint, render_template


project_api  = Blueprint('project_api',__name__,template_folder='templates',static_folder='static')
engine = create_engine(
    'postgresql://postgres:postgres@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session() 

@project_api.route('/create_new_project')
def create_new_project():
    return "Create New Project"

@project_api.route('/create_new_task')
def create_new_task():
    return "Create New Task"

@project_api.route('/edit_task')
def edit_task():
    return "Edit Task"

@project_api.route('/delete_task')
def delete_task():
    return "Delete Task"

@project_api.route('/project_dashboard')
def project_dashboard():
    return render_template('projects/dashboard.html')


@project_api.route('/settings')
def settings():
    return render_template('projects/settings.html')