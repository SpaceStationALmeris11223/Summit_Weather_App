from flask import Blueprint, render_template, session,request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from .weather import get_weather
from .models import User, db
from markupsafe import escape
#blocks profanity, so no slurs etc go into the username & passwords.
#if you want to use this just type
#pip install better_profanity
from better_profanity import profanity

import re

main = Blueprint('main', __name__)

profanity.load_censor_words()

"""
Home Route starts↓
"""
@main.route('/')
def home():
    latitude = 44.9778  # Example default: Minneapolis
    longitude = -93.2650
    weather_data = get_weather(latitude, longitude)
    return render_template('index.html', 
                         weather=weather_data,
                         latitude=latitude,
                         longitude=longitude)
"""
Main Route ends↑"""
"""
Validation functions route start↓
"""
#defines what↓ a valid username is
def valid_username(username):
    if not re.match(r"^[a-zA-Z0-9_]{3,20}$", username):
        return False,   "Username must be between 3 - 20 characters, letters, numbers, underscores only."     
#Usernames cannot contain profanity↓
    if profanity.contains_profanity(username):
        return False,    "Inappropriate word detected"
    return True, ""
#defines what↓ a valid password is
def valid_password(password):
    errors = []
#Must be at least 8 Char↓
    if len(password) < 8:
        errors.append("Password must be at least 8 characters")
#must have at least 1 letter↓
    if not re.search(r"[a-zA-Z]", password):
       errors.append("Password must include at least one letter.")
#must have at least 1number 
    if not re.search(r"\d", password):
        errors.append("Password must include at least one number")
#must have at least 1 punctuation mark
    if not re.search(r'[!@#$%^&*()_+\[\]{};:\'",.<>/?\\|`~]', password):
        errors.append("Password must contain at least one special character")
#pword cannot contain profanity
    if profanity.contains_profanity(password):
        errors.append("Username or password contains innaporpriate language")
    return errors

"""
Validation functions route end↑
"""

""""
User registration route starts↓
"""
@main.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
    #sanatize user input(clean up)
        username = escape(request.form.get("username", "").strip())
        password = request.form.get("password", "")

        valid_user, bad_u_msg = valid_username(username)
        #Username Check↓
        if valid_user:
            flash(bad_u_msg)
            return redirect(url_for("main.register"))
        
        valid_pass = valid_password(password)
        if valid_pass:
            flash("Password must inlcude: "+", ".join(valid_pass))
            return redirect(url_for("main.register"))
        
        #checks if user already exist↓
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username is already taken.")
            return redirect(url_for("main.register"))
        
#creates and ↓saves user
        new_user = User(username=username)
        new_user.set_password(password)
#takes the ↑raw password and creates a hashed version (examp: 2dsf6ads1f) and stores it

#creates user and auto logs them in
        db.session.add(new_user)
        db.session.commit()#saves the user data to database
#should auto load the user once accounts↓ is down might be more touble than worth
        session["user_id"] = new_user.id
        flash("Account created successfully! Welcome.")
        return redirect(url_for("main.home"))
    return render_template("register.html")
#should auto load the user once↑ accounts is down might be more touble than worth
#Shpould I redirect them to the homepage?

"""
Login Route Starts ↓
"""
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = escape(request.form.get("username", "").strip())
        password = request.form.get("password", "")

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session["user_id"] = user.id
            flash("Logg in successful!")
            return redirect(url_for("main.home"))
        else:
            flash("invalid Username or password.")
            return redirect(url_for("main.login"))
    return render_template("login.html")
"""
Login route ends ↑
"""
"""
Logout route starts ↓
"""
@main.route('/logout')
def logout():
    session.clear()
#clears all↑ session data including user id
    flash("You have been logged out.")
    return redirect(url_for("main.home"))
"""
Logout route ends↑
"""
"""
Account route starts↓
"""
@main.route('/account')
def account():
    if "user_id" not in session:
        flash("Pleas log in to access your account.")
        return redirect(url_for('main.login'))
    
#if user is logged in ↓
    return render_template("account.html")