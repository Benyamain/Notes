from flask import Blueprint, render_template, request

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
        password_one = request.form.get('password-one')
        password_two = request.form.get('password-two')

        if len(email) < 4:
            pass
        elif len(first_name) < 2:
            pass
        elif len(password_one) != password_two:
            pass
        elif len(password_one) < 7:
            pass
        else:
            # Add user to database
            pass
    
    return render_template("signup.html")