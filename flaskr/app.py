import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_migrate import Migrate
from models.database import db
from models.CompanyAdmin import CompanyAdmin
from models.Employee import Employee



# Importa tus módulos personalizados
from routes.web import web_bp

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{BASE_DIR}/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'magneto'

db.init_app(app)
 
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'web.login'

@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))


with app.app_context():
    print("Creating database tables...")
    db.create_all()
    print("Tables created successfully")
    print(f"Database is located at: {app.config['SQLALCHEMY_DATABASE_URI']}")



app.register_blueprint(web_bp)


# Inicialización de SQLAlchemy

# Configuración de Flask-Login

# Registro de blueprints

if __name__ == '__main__':
    app.run(debug=True)

