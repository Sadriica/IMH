from flask import Blueprint

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

@web_bp.route("/data/show", endpoint="show")
def datos_grafica_route():
    return data.show()

