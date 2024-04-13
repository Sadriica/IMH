from flask import Flask, redirect, url_for, render_template, Blueprint

def index():    
    return render_template('index.html')
def login():
    return render_template('login.html')
def register():
    return render_template('register.html')
def profile():
    return render_template('profile.html')
def register_response():
    return render_template('register_response.html')
def forgot_password():
    return render_template('forgot_password.html')

