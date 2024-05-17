from flask import Blueprint
from flask import request, redirect, url_for, render_template
from models import CompanyAdmin
from models.database import db

import os

ROOT_DIR = os.environ.get('ROOT_DIR')

user_controller_path = os.path.join(ROOT_DIR, 'controllers', 'user_controller.py')
data_controller_path = os.path.join(ROOT_DIR, 'controllers', 'data_controller.py')

from controllers import user_controller as user

from controllers import data_controller as data

auth_bp = Blueprint('auth', __name__)


