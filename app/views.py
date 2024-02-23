from flask import Blueprint, render_template
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/login')
def login():
    return render_template('login.html')

@views.route('/logout')
def logout():
    return "<h2> logout </h2>"

@views.route('/signup')
def signup():
    return render_template('signup.html')
