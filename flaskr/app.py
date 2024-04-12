from flask import Flask

from flask_login import LoginManager

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

os.environ['ROOT_DIR'] = ROOT_DIR

from routes.web import web_bp

app = Flask(__name__)

#App routes
app.register_blueprint(web_bp)


#app.config['SECRET_KEY'] = 'tu_clave_secreta'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db

# Migración de la base de datos

#migrate = Migrate(app, db)

# Configuración del administrador de inicio de sesión

#login_manager = LoginManager(app)

#login_manager.login_view = 'login'  # Nombre de la función de inicio de sesión

if __name__ == '__main__':
    
    app.run(debug=True)
