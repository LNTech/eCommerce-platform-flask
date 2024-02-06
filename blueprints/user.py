# admin_blueprint.py
from models import db, User
from utility import check_form_data

from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("user/register.html")
    
    elif request.method == "POST":
        username = request.form.get("email")
        password = request.form.get("password")
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        address_line_1 = request.form.get("address_line_1")
        address_line_2 = request.form.get("address_line_2")
        city = request.form.get("city")
        county = request.form.get("county")
        postcode = request.form.get("postcode")

        # This is a terrible line of code that I'll change after I've finished testing register/logins
        if check_form_data(username, password, fname, lname, address_line_1, city, county, postcode) is False:
            flash('Problem with information provided.')
            return render_template("user/register.html")
        
        email_exists = User.query.filter_by(email=username.lower()).first()
        if email_exists:
            flash('Email already registered.')
            return render_template("user/register.html")
        
        password_hash = generate_password_hash(password, method='pbkdf2:sha256')

        new_user = User(
            email=username.lower(),
            password=password_hash,
            fname=fname.title(),
            lname=lname.title(),
            address_line_1=address_line_1.title(),
            address_line_2=address_line_2.title(),
            city=city.title(),
            county=county.title(),
            postcode=postcode.upper()
        )

        db.session.add(new_user)
        db.session.commit()

        flash('User registered succesfully.')
        return redirect(url_for("user.login"))
        
@user_blueprint.route('/logout', methods=["GET"])
def logout():
    if session.get('logged_in') is True:
        session.pop('logged_in')
        session.pop('username')

    return redirect(url_for('user.login'))

@user_blueprint.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("user/login.html")
    
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if check_form_data(email, password) is False:
            flash('Problem with username or password.')
            return render_template("user/login.html")

        user_exists = User.query.filter_by(email=email.lower()).first()
        if user_exists is None:
            flash('No user found with that email.')
            return render_template("user/login.html")
        
        if check_password_hash(user_exists.password, password) is False:
            flash('Invalid username or password.')
            return render_template("user/login.html")
        
        session['logged_in'] = True
        session['username'] = user_exists.email
        return redirect(url_for("index"))

    return jsonify({"message": "Unrecognized request type"}), 405