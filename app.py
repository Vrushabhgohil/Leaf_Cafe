import os
from flask import Flask, redirect, request
from flask_login import LoginManager
from common.database import db
from common.model import Users
from tenants.user_api.api import user_api
from tenants.project_api.api import project_api
from dotenv import load_dotenv

def create_app():
    app=Flask(__name__)
    load_dotenv()
    database_uri = os.getenv('DATABASE_URI')
    secret_key = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = secret_key
   
    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    app.register_blueprint(user_api)
    app.register_blueprint(project_api)
    return app


app=create_app()
login_manager = LoginManager()
login_manager.init_app(app) 

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

def add_photo(file):
    photos_path = os.path.join(os.getcwd(), 'static', 'photos')
    UPLOAD_FOLDER = photos_path
    folder = app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    filename = file.filename
    file.save(os.path.join(folder, filename))

@app.before_request
def before_request():
    tenant = request.headers.get('tenant')
    if tenant:
        db.choose_tenant(tenant)
        db.create_all()

@app.route('/')
def home():
    return "Hello World"
   
if __name__ == '__main__':  
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)