from flask import Blueprint
from flask import request, redirect, url_for, render_template
from models import db, CompanyAdmin

import os

ROOT_DIR = os.environ.get('ROOT_DIR')

user_controller_path = os.path.join(ROOT_DIR, 'controllers', 'user_controller.py')
data_controller_path = os.path.join(ROOT_DIR, 'controllers', 'data_controller.py')

from controllers import user_controller as user

from controllers import data_controller as data

auth_bp = Blueprint('auth', __name__)

# Define las rutas y las funciones de las vistas aquí

@auth_bp.route("/main", endpoint="index")

@auth_bp.route("/register_company", methods=['POST'])
def register_company():
    print(request.form)
    company_name = request.form['company_name']
    business_name = request.form['business_name']
    main_email = request.form['main_email']
    person_in_charge = request.form['person_in_charge']
    role_in_company = request.form['role_in_company']
    one_time_password = request.form['one_time_password']

    new_company = CompanyAdmin(
        company_name=company_name,
        business_name=business_name,
        main_email=main_email,
        person_in_charge=person_in_charge,
        role_in_company=role_in_company,
        one_time_password=one_time_password
    )
    db.session.add(new_company)
    db.session.commit()

    return redirect(url_for('some_page')) 
