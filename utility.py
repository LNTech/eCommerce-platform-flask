from models import db, Category, Subcategory, CategorySubcategoryMap

def check_form_data(*args):
    for arg in args:
        if arg is None or arg == "":
            return False
    return True


def get_subcategories():
    subcategories = Subcategory.query.all()

    filtered = [] 

    for category in subcategories:
        filtered.append({
            "name": category.name,
            "public_id": category.public_id,
        })

    return filtered


def get_categories():
    categories = Category.query.all()

    filtered = [] 

    for category in categories:
        subcategories = []
        joins = CategorySubcategoryMap.query.filter_by(category_id=category.id).all()

        for join in joins:
            subcategory = Subcategory.query.filter_by(id=join.subcategory_id).first() 
            subcategories.append({
                "name": subcategory.name,
                "public_id": subcategory.public_id
            })
        
        filtered.append({
            "name": category.name,
            "public_id": category.public_id,
            "subcategories": subcategories
        })

    return filtered