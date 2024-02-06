# admin_blueprint.py
from models import db, Category, Subcategory, CategorySubcategoryMap

from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
import uuid
from utility import get_categories, get_subcategories, check_form_data
admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/panel', methods=["GET", "POST"])
def admin_panel():
    return render_template("admin/panel.html", categories=get_categories(), subcategories=get_subcategories())


@admin_blueprint.route("/panel/subcategory/assign", methods=["POST"])
def assign_subcategory():
    category = request.form.get("category_assign")
    subcategory = request.form.get("subcategory_assign")

    if check_form_data(category, subcategory) is False:
        return redirect(url_for('admin.admin_panel'))

    print(category, subcategory)
    category_exists = Category.query.filter_by(public_id=category).first()
    subcategory_exists = Subcategory.query.filter_by(public_id=subcategory).first()

    if category_exists is None or subcategory_exists is None:
        print("Nope")
        return redirect(url_for('admin.admin_panel'))
    
    join_exists = CategorySubcategoryMap.query.filter_by(category_id=category_exists.id, subcategory_id=subcategory_exists.id).first()
    if join_exists:
        print("Nope")
        return redirect(url_for('admin.admin_panel'))
        
    new_join = CategorySubcategoryMap(category_id=category_exists.id, subcategory_id=subcategory_exists.id)
    db.session.add(new_join)
    db.session.commit()

    return redirect(url_for('admin.admin_panel'))


@admin_blueprint.route("/panel/category/add", methods=["POST"])
def add_category():
    category = request.form.get("category")

    category_exists = Category.query.filter_by(name=category.title()).first()

    if category_exists:
        flash('Category already added.')
        return redirect(url_for('admin.admin_panel'))
    
    new_category = Category(name=category.title(), public_id=str(uuid.uuid4()))
    db.session.add(new_category)
    db.session.commit()

    return redirect(url_for('admin.admin_panel'))


@admin_blueprint.route("/panel/subcategory/add", methods=["POST"])
def add_subcategory():
    subcategory = request.form.get("subcategory")

    subcategory_exists = Subcategory.query.filter_by(name=subcategory.title()).first()

    if subcategory_exists:
        flash('Subcategory already added.')
        return redirect(url_for('admin.admin_panel'))
    
    new_subcategory = Subcategory(name=subcategory.title(), public_id=str(uuid.uuid4()))
    db.session.add(new_subcategory)
    db.session.commit()

    return redirect(url_for('admin.admin_panel'))