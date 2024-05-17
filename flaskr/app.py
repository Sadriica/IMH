import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.database import db
from models.CompanyAdmin import CompanyAdmin
from models.Employee import Employee



# Importa tus módulos personalizados
from routes.web import web_bp

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__)
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASE_DIR}/app.db'  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'magneto'

    db.init_app(app)
    app.register_blueprint(web_bp)

    from models.CompanyAdmin import CompanyAdmin
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("Tables created successfully")
        print(f"Database is located at: {app.config['SQLALCHEMY_DATABASE_URI']}")
    return app


# Inicialización de SQLAlchemy

# Configuración de Flask-Login

# Registro de blueprints

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

