from flask import Blueprint

# Define file is a blue print that has the routes and views
views = Blueprint('views', __name__)

# Decorator
@views.route('/')
def home():
    return "<h1>Test</h1>"