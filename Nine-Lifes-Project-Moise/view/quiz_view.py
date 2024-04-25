from flask import Blueprint, request
from controller.quiz_controller import *


quizView = Blueprint('quiz', __name__, url_prefix='/quiz')


@quizView.route('/')
def home():
    return "<center><h1>Welcome to the QUIZ VIEW</h1></center>"


@quizView.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        id_category = request.form.get('id_category')
        question = request.form.get('question')
        option1 = request.form.get('option1')
        option2 = request.form.get('option2')
        option3 = request.form.get('option3')
        option4 = request.form.get('option4')
        correct = request.form.get('correct')
        return save_quiz(id_category, question, option1, option2, option3, option4, correct)