from flask import request, redirect, url_for, render_template, flash
from werkzeug.security import generate_password_hash
from .models  import db, User
from markupsafe import escape
from better_profantiy import profanity
import re




@main.route("/register', methods=['GET', 'POST']")
def register():
    if request.method =="POST":
#cleans up the form inputs↓
        username = escape(request.form.get("Username", "").strip())
        password = request.form.get("password", "").strip()
        
#validate username input
        if not re.match(r"^[a-zA-Z0-9_]{3,20}$", username):
            flash("Username must be 3-20 characters, letter/numbers only.")
            return redirect(url_for("main.home"))

    #validate password input
        if (len(password) < 8 or
            not re.search(r'[a-zA-Z]', password)):
            not re.search(r'\d', password)
            not re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
            flash("Password must be 8+characters, includes letters, numbers,and symbols.")
            return redirect(url_for("main.home"))
        
    #profanity check
        if profanity.contains_profanity(username) or profanity.contains_profanity(password):
            flash("Username or password uses inappropriate language")
            return redirect(url_for("main.home"))

    #store user using set_passoword
        new_user = User(username=username)
        new_user.set_password(password)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash("Account created")
            return redirect(url_for("main.home"))
        except:
            db.session.rollback()
            flash("Username already exist or an error occurred.")
            return redirect(url_for("main.register"))
    return render_template("main.home")