from flask import Blueprint, request, render_template, redirect, url_for
from controllers.category import * 



category_view = Blueprint('category', __name__, url_prefix='/category')


@category_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        categories = get_all_categories()
        return render_template('categories.html', categories=categories)
    elif request.method == 'POST':
        category_name = request.form['category_name']
        category = save_category(category_name)
        return redirect(url_for('category.get_or_update_instance', id_category=category.id_category))


@category_view.route('/<id_category>', methods=['GET', 'POST'])
def get_or_update_instance(id_category):
    if request.method == 'GET':
        category = get_category_with_id(id_category)
        return render_template('category.html', category=category)
    elif request.method == 'POST':
        category_name = request.form['category_name']
        save_category(category_name, id_category=id_category)
        return redirect(url_for('category.get_or_update_instance', id_category=id_category))