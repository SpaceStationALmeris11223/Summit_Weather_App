from flask import request, redirect, url_for, render_template, flash,session
from werkzeug.security import generate_password_hash
from .models  import db, User
from markupsafe import escape
from better_profantiy import profanity
import re




@main.route("/register", methods=['GET', 'POST'])
def register():
    if request.method =="POST":
        
#cleans up the form inputs↓
        username = escape(request.form.get("username", "").strip())
        password = request.form.get("password", "").strip()
        
 
def valid_username(username):
#validate username input
        if not re.match(r"^[a-zA-Z0-9_]{3,20}$", username):
            flash("Username must be 3-20 characters, letter/numbers only.")
            return redirect(url_for("main.register"))
        if profanity.contains_profanity(username):
            flash("Username contains inappropriate langauge.")
            return redirect(url_for("main.register"))

def valid_password(password):
    #validate password input

        if len(password) < 8:
            flash("Password must be at least 8 characters")
            return False
        if not re.search(r'[a-zA-Z]', password):
            flash("Password must include at least one letter.")
            return False
        if not re.search(r'\d', password):
            flash("Password must include at least one number")
            return False
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            flash("Password must contain at least one special character")
            return False
        return True

 

@main.route("/register", methods=['GET', 'POST'])
def register():
    if request.method =="POST":    
        #cleans up the form inputs↓
        username = escape(request.form.get("username", "").strip())
        password = request.form.get("password", "").strip()     


            #validate inputs
        username_invalid = valid_username(username)
        password_invalid = valid_password(password)
        #username check
        if username_invalid:
                for error in username_invalid:
                    flash(error)
                return redirect(url_for("main.register"))
        #password check
        if password_invalid:
            for error in password_invalid:
                    flash(error)
            return redirect(url_for("main.register"))
            #if username exist
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exist.")
            return redirect(url_for("main.register"))

        #create new user
        new_user = User(username=username)
        new_user.set_password(password)
        try:
            db.session.add(new_user)
            db.session.commit()
            session["user_id"] = new_user.id #auto login
            flash("Account created!")
            return redirect(url_for("main.home"))
        except Exception as e:
            db.session.rollback()
            flash("error occurred during registration.")
            return redirect(url_for("main.register"))
    return render_template("register.html")
