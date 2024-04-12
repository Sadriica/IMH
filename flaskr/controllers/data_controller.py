from flask import Flask, redirect, url_for, render_template, Blueprint

import os



ROOT_DIR = os.environ.get('ROOT_DIR')

user_controller_path = os.path.join(ROOT_DIR, 'utils', 'main.py')




