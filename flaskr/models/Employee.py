
from flask_login import UserMixin
from sqlalchemy.schema import ForeignKeyConstraint
from models.database import db
from models.CompanyAdmin import CompanyAdmin

class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company_admin.id'), nullable=False)
    position = db.Column(db.String(100), nullable=False)

    company = db.relationship('CompanyAdmin', backref=db.backref('employees', lazy=True))

    def __repr__(self):
        return f'<Employee {self.name}>'

