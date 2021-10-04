from app import test_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(test_app())


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    project_name = db.Column(db.String(50), nullable=False)

    def __init__(self, name, password, project_name):
        self.name = name
        self.password = password
        self.project_name = project_name

