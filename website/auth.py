from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import database
from werkzeug.security import generate_password_hash, check_password_hash

# Hashing function has no inverse
# Given some x, you can find the y, but not the other way around
# Given the hash output, you can never return to the stored password
# x -> y
# f(x) = x + 1
# f'(x) = y - 1
# y -> x


# Backend
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # Returns the first email that comes up if any
        user = User.query.filter_by(email=email).first()

        if (user):
            # Hash the first and compare it to the hashed password created
            # when user signed up
            if check_password_hash(user.password, password):
                flash('Login success!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect passsword! Please try again.', category='error')
        else:
            flash('Email does not exist!', category='error')

    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        password_one = request.form.get('password-one')
        password_two = request.form.get('password-two')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists!', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name be greater than 1 character.', category='error')
        elif len(last_name) < 2:
            flash('Last name be greater than 1 character.', category='error')
        elif password_one != password_two:
            flash('Passwords do not match.', category='error')
        elif len(password_one) < 7:
            flash('Password must be at least 6 characters.', category='error')
        else:
            # Add user to database
            new_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(password_one, method='sha256'))
            database.session.add(new_user)
            # Update the database with new user
            database.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    
    return render_template("signup.html")