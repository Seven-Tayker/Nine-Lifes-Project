from flask import Blueprint, request
from controller.category_controller import *

categoryView = Blueprint('category', __name__, url_prefix='/category')


@categoryView.route('/')
def home():
    return "<center><h1>Welcome to the CATEGORY VIEW</h1></center>"


@categoryView.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        category_name = request.form.get('category_name')
        nb_of_questions = request.form.get('nb_of_questions')
        return save_category(category_name, nb_of_questions)