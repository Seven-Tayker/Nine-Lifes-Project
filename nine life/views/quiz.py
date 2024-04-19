from flask import Blueprint, request
from controllers.quizController import QuizController

quiz_view = Blueprint('quiz', __name__, url_prefix='/quiz')

@quiz_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        return QuizController.get_all_quizzes()
    else:
        submitted_data = request.form

        id_category = submitted_data['id_category']
        question = submitted_data['question']
        option1 = submitted_data['option1']
        option2 = submitted_data['option2']
        option3 = submitted_data['option3']
        option4 = submitted_data['option4']
        correct_answer = submitted_data['correct']

        return QuizController.create_quiz(id_category, question, option1, option2, option3, option4, correct_answer)

@quiz_view.route('/<quiz_id>', methods=['GET', 'POST'])
def get_or_update_instance(quiz_id):
    if request.method == 'GET':
        return QuizController.get_quiz_with_id(quiz_id)
    else:
        submitted_data = request.form

        id_category = submitted_data['id_category']
        question = submitted_data['question']
        option1 = submitted_data['option1']
        option2 = submitted_data['option2']
        option3 = submitted_data['option3']
        option4 = submitted_data['option4']
        correct_answer = submitted_data['correct']

        return QuizController.update_quiz(quiz_id, id_category, question, option1, option2, option3, option4, correct_answer)