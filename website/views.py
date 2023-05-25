from flask import Blueprint, render_template

# Define file is a blue print that has the routes and views
views = Blueprint('views', __name__)

# Decorator
@views.route('/')
def home():
    return render_template("home.html")