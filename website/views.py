from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import database
import json

# Define file is a blue print that has the routes and views
views = Blueprint('views', __name__)

# Decorator
@views.route('/', methods=['GET', 'POST'])
# You cannot get the home page unless you are logged in
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(note_data=note, user_id=current_user.id)
            database.session.add(new_note)
            database.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    # Load the data from the post request
    note = json.loads(request.data)
    note_id = note['noteId']
    note = Note.query.get(note_id)

    if note:
        # Perform a security check to only delete notes if
        # signed in on that account
        if note.user_id == current_user.id:
            database.session.delete(note)
            database.session.commit()
    
    # Empty
    return jsonify({})