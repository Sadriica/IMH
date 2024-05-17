from flask import Blueprint
from flask import request, redirect, url_for, render_template,flash
from models.CompanyAdmin import CompanyAdmin
from models.database import db


import os

ROOT_DIR = os.environ.get('ROOT_DIR')

user_controller_path = os.path.join(ROOT_DIR, 'controllers', 'user_controller.py')
data_controller_path = os.path.join(ROOT_DIR, 'controllers', 'data_controller.py')

from controllers import user_controller as user

from controllers import data_controller as data

web_bp = Blueprint('web', __name__)

# Define las rutas y las funciones de las vistas aquí



@web_bp.route("/main", endpoint="index")
def index_route():
    return user.index()

@web_bp.route("/login", endpoint="login")
def login_route():
    return user.login()

@web_bp.route("/register", endpoint="register")
def register_route():
    return user.register()

@web_bp.route("/profile_admin", endpoint="profile_admin")
def profile_admin_route():
    return user.profile_admin()

@web_bp.route("/profile", endpoint="profile")
def profile_route():
    return user.profile()

@web_bp.route("/register_response", endpoint="register_response")
def register_response_route():
    return user.register_response()

@web_bp.route("/forgot_password", endpoint="forgot_password")
def profile_route():
 return user.register()
@web_bp.route("/register_company", methods=['POST'])
def register_company():
    print(request.form)
    company_name = request.form['company_name']
    business_name = request.form['business_name']
    main_email = request.form['main_email']
    person_in_charge = request.form['person_in_charge']
    role_in_company = request.form['role_in_company']
    one_time_password = request.form['one_time_password']

    existing_company = CompanyAdmin.query.filter_by(main_email=main_email).first()
    if existing_company:
        flash('Error: El correo electrónico principal ya está registrado.')
        return redirect(url_for('web.index')) 


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

    return redirect(url_for('web.profile_admin')) 
