# from __init__.py
from . import database
from flask_login import UserMixin
from sqlalchemy.sql import func

# One-to-many constraint

class Note(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    note_data = database.Column(database.String(250000))
    # Do not need to specify date using func
    note_date = database.Column(database.DateTime(timezone=True), default=func.now())
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'))

# Defining a schema
class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(45), unique=True)
    password = database.Column(database.String(45))
    first_name = database.Column(database.String(45))
    last_name = database.Column(database.String(45))
    # Essentially stores the list of notes for each user
    notes = database.relationship('Note')