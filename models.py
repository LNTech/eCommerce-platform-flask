# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(72), nullable=False)
    fname = db.Column(db.String(32), nullable=False)
    lname = db.Column(db.String(32), nullable=False)
    address_line_1 = db.Column(db.String, nullable=False)
    address_line_2 = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=False)
    county = db.Column(db.String, nullable=False)
    postcode = db.Column(db.String(12), nullable=False)


class Category(db.Model):
    __tablename__ = "Categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    public_id = db.Column(db.String, unique=True, nullable=False)


class Subcategory(db.Model):
    __tablename__ = "Subcategories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    public_id = db.Column(db.String, unique=True, nullable=False)


class CategorySubcategoryMap(db.Model):
    __tablename__ = "CategorySubcategoryMap"

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('Categories.id'))
    subcategory_id = db.Column(db.Integer, db.ForeignKey('Subcategories.id'))