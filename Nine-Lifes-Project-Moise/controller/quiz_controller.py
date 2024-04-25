from model.quiz_model import Quiz


def save_quiz(id_category, question, option1, option2, option3, option4, correct):
    quiz = Quiz(id_category=id_category, question=question, option1=option1, option2=option2, option3=option3,
                option4=option4, correct=correct)
    quiz.save()
    return quiz.toJSON()


def get_all_quizzes():
    quiz = Quiz()
    return quiz.read()


def get_quiz_with_id(id_quiz):
    quiz = Quiz()
    return quiz.read(id_quiz)


def update_quiz(id_quiz, id_category, question, option1, option2, option3, option4, correct):
    quiz = Quiz(id_quiz=id_quiz, id_category=id_category, question=question, option1=option1, option2=option2,
                option3=option3, option4=option4, correct=correct)
    quiz.save()
    return quiz.toJSON()


def delete_quiz_with_id(id_quiz):
    quiz = Quiz(id_quiz=id_quiz)
    quiz.delete()
    returnSure! I apologize for the incomplete response. Here's the complete `quiz_controller.py` code:

```python
from model.quiz_model import Quiz


def save_quiz(id_category, question, option1, option2, option3, option4, correct):
    quiz = Quiz(id_category=id_category, question=question, option1=option1, option2=option2, option3=option3,
                option4=option4, correct=correct)
    quiz.save()
    return quiz.toJSON()


def get_all_quizzes():
    quiz = Quiz()
    return quiz.read()


def get_quiz_with_id(id_quiz):
    quiz = Quiz()
    return quiz.read(id_quiz)


def update_quiz(id_quiz, id_category, question, option1, option2, option3, option4, correct):
    quiz = Quiz(id_quiz=id_quiz, id_category=id_category, question=question, option1=option1, option2=option2,
                option3=option3, option4=option4, correct=correct)
    quiz.save()
    return quiz.toJSON()


def delete_quiz_with_id(id_quiz):
    quiz = Quiz(id_quiz=id_quiz)
    quiz.delete()
    return quiz.toJSON()


def delete_all_quizzes():
    quiz = Quiz()
    quiz.delete()
    return True