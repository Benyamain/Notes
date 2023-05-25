from flask import Blueprint, render_template, request, flash

# Backend
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
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

        if len(email) < 4:
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
            flash('Account was created!', category='success')
    
    return render_template("signup.html")