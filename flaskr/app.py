import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.CompanyAdmin import CompanyAdmin
from models.Employee import Employee

# Importa tus módulos personalizados
from routes.web import web_bp

app = Flask(__name__)

# Configuración básica de la aplicación
app.config['SECRET_KEY'] = 'magneto'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de SQLAlchemy
db = SQLAlchemy(app)

# Configuración de Flask-Login

# Registro de blueprints
app.register_blueprint(web_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

