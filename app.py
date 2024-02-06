from flask import Flask, render_template, request, jsonify, flash, session, redirect, url_for

from models import db, Category, Subcategory, CategorySubcategoryMap
from blueprints.user import user_blueprint
from blueprints.admin import admin_blueprint



app = Flask(__name__)

app.secret_key = 'tmp_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Change this to your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(user_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")




@app.route('/')
def index():
    return render_template("index.html")

@app.route('/products', methods=["GET", "POST"])
def products():
    return ""


@app.route('/categories', methods=["GET", "POST"])
def categories():
    return ""


@app.route('/subcategories', methods=["GET", "POST"])
def subcategories():
    return ""
                       

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
