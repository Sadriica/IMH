from flask import Flask, redirect, url_for, render_template, Blueprint

def index():    
    return render_template('index.html')
def login():
    return render_template('login.html')
def register():
    return render_template('register.html')
