import os

from model.question_model import Question
# from .files import save_file

# from werkzeug.utils import secure_filename

from constants import PATH_TO_DB


def get_all_questions():
    return Question.read()


def get_question_model_with_id(id):
    return Question.read(id)


def save_question_model(id=None, question_text, answer_text, category_id=None, difficulty_id=None, points):
    if id != None:
        question_model = get_question_model_with_id(id)
        question_model.question_text, question_model.answer_text, question_model.points = (
            question_text, answer_text, points
        )
    else:
        question_model = Question(
            question_text=question_text, answer_text=answer_text,
            points=points
        )

    questions.save()

    return question_model


def delete_question_model(id):
    question_model = get_question_model_with_id(id)
    question_model.delete()