import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.database import db
from models.CompanyAdmin import CompanyAdmin
from models.Employee import Employee



# Importa tus módulos personalizados
from routes.web import web_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.register_blueprint(web_bp)

    from models.CompanyAdmin import CompanyAdmin

    return app


# Inicialización de SQLAlchemy

# Configuración de Flask-Login

# Registro de blueprints

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

