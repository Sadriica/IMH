from flask import Flask, redirect, url_for, render_template, Blueprint



def index():
    
    return render_template('index.html')
