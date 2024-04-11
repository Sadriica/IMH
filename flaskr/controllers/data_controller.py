from flask import Flask, redirect, url_for, render_template, Blueprint

import os



ROOT_DIR = os.environ.get('ROOT_DIR')

user_controller_path = os.path.join(ROOT_DIR, 'utils', 'main.py')

from utils.main import values_usage_cost, values_usage_kw, values_usage_sum, devices, time, graphics

def grafic():
    route = graphics()
    
    return render_template('grafic.html', ruta = route)


def show():
    

    
    return render_template('show.html',cost=values_usage_cost,kw=values_usage_kw,sum=values_usage_sum, items = devices, tiempo = time)



