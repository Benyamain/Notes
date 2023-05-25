from flask import Blueprint, render_template
from flask_login import login_required, current_user

# Define file is a blue print that has the routes and views
views = Blueprint('views', __name__)

# Decorator
@views.route('/')
# You cannt get the home page unless you are logged in
@login_required
def home():
    return render_template("home.html")