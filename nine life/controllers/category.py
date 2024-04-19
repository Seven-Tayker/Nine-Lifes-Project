import os

from models.category import Category


def get_all_categories():
    return Category.read()


def get_category_with_id(id_category):
    return Category.readById(id_category)


def save_category(category_name, id_category=None):
    if id_category is not None:
        category = get_category_with_id(id_category)
        category.category_name = category_name
        category.update(id_category)
    else:
        category = Category(category_name=category_name)
        category.create()

    return category


def delete_category(id_category):
    category = get_category_with_id(id_category)
    if category is not None:
        quizzes = quizController.get_quizzes_by_category(id_category)
        for quiz in quizzes:
            quizController.delete_quiz(quiz.id_quiz)
        category.deleteById(id_category)