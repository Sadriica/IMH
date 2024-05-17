from flask import Blueprint
from flask import request, redirect, url_for, render_template,flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from models.CompanyAdmin import CompanyAdmin
from models.Employee import Employee
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


@web_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        company_id = request.form['company_id']
        employee = Employee.query.filter_by(email=email, company_id=company_id).first()
        if employee and employee.password == password:
            login_user(employee)
            flash('Inicio de sesión exitoso.')
            return redirect(url_for('web.manage_employees'))
        else:
            flash('Correo electrónico, contraseña o compañía incorrectos.')
    companies = CompanyAdmin.query.all()
    return render_template('../templates/login.html', companies=companies)

@web_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión.')
    return redirect(url_for('web.login'))

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

@web_bp.route('/employees', methods=['GET', 'POST'])
def manage_employees():
    if request.method == 'POST':
        action = request.form['action']
        if action == 'create':
            name = request.form['name']
            password = request.form['password']
            company_id = request.form['company_id']
            position = request.form['position']
            try:
                new_employee = Employee(name=name, password=password, company_id=company_id, position=position)
                db.session.add(new_employee)
                db.session.commit()
                flash('Empleado creado con éxito.')
            except Exception as e:
                db.session.rollback()
                flash(f'Error al crear empleado: {e}')
                return redirect(url_for('web.manage_employees'))
        elif action == 'edit':
            employee_id = request.form['employee_id']
            employee = Employee.query.get(employee_id)
            if employee:
                try:
                    employee.name = request.form['name']
                    employee.password = request.form['password']
                    employee.company_id = request.form['company_id']
                    employee.position = request.form['position']
                    db.session.commit()
                    flash('Empleado actualizado con éxito.')
                except Exception as e:
                    db.session.rollback()
                    flash(f'Error al actualizar empleado: {e}')
                    return redirect(url_for('web.manage_employees'))
            else:
                flash('Empleado no encontrado.')
                return redirect(url_for('web.manage_employees'))
        elif action == 'delete':
            employee_id = request.form['employee_id']
            employee = Employee.query.get(employee_id)
            if employee:
                try:
                    db.session.delete(employee)
                    db.session.commit()
                    flash('Empleado eliminado con éxito.')
                except Exception as e:
                    db.session.rollback()
                    flash(f'Error al eliminar empleado: {e}')
                    return redirect(url_for('web.manage_employees'))
            else:
                flash('Empleado no encontrado.')
                return redirect(url_for('web.manage_employees'))

   
@web_bp.route('/companies_check', methods=['GET', 'POST'])
def companiescheck():
    employees = Employee.query.all()
    companies = CompanyAdmin.query.all()
    print(f"Found {len(companies)} companies")  # Agregar depuración
    if not companies:
        flash('No hay compañías disponibles.')
    return render_template('profile_admin.html', employees=employees, companies=companies)

