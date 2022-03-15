import re
from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')

def index():
    stuff="This is <strong>Bold</strong> Text"
    favourite_pizza=["cheese","mushroom","paparoni",31]
    
    return render_template("index.html",stuff=stuff,favourite_pizza=favourite_pizza)

@app.route('/user/<name>')

def user(name):
    return render_template("user.html",user_name=name)   

@app.errorhandler(404)

def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500)

def internal_server_error(e):
    return render_template("500.html"),500
