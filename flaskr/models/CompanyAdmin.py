
from database import db

class CompanyAdmin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    business_name = db.Column(db.String(100), nullable=False)
    main_email = db.Column(db.String(120), unique=True, nullable=False)
    person_in_charge = db.Column(db.String(100), nullable=False)
    role_in_company = db.Column(db.String(100), nullable=False)
    one_time_password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<CompanyAdmin {self.company_name}>'
      
