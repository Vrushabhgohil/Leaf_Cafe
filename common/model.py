from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import Boolean, Column, DateTime, ForeignKey,Integer, String
from common.database import db

class User(UserMixin, db.Model):
    __tablename__ = 'User'
    __table_args__ = {'schema': 'myschema'}
    id = Column(String(100), primary_key=True)
    name = Column(String(250), nullable=False)
    dp_addr = Column(String(250),nullable=False,default='dummy-profile-pic-male1.jpg')
    email = Column(String(50), unique=True, nullable=False)
    phone = Column(String(10), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=None)
    is_active = Column(Boolean, default=True)


class Project(db.Model):
    __tablename__ = 'Project'
    __table_args__ = {'schema': 'myschema'}
    project_id = Column(String(100), primary_key=True)
    project_name = Column(String(500), nullable=False)
    project_head =Column(String(50),ForeignKey('myschema.User.id'),nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    end_at = Column(DateTime, default=None)
    project_status = Column(Boolean,default=True)
    project_summary = Column(String(150))
    project_git_link = Column(String(150))
    user = db.relationship('User',primaryjoin=(User.id == project_head))

class Contributor(db.Model):
    __tablename__ = 'Contributor'
    cont_id = Column(String(100), primary_key=True)
    cont_user_id = Column(String(100))
    cont_email = Column(String(50), unique=True, nullable=False)
    cont__task = Column(String(50), nullable=False)

class Task(db.Model):
    __tablename__ = 'Task'
    task_id = Column(String(50), primary_key=True)
    task_title = Column(String(150), unique=True, nullable=False)
    task_desc = Column(String(500), nullable=False)
    task_date = Column(DateTime,default=datetime.now)
    task_status = Column(String(15))


