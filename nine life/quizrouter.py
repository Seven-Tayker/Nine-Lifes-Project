from controllers.quizController import *
from flask import Blueprint, jsonify, request

# Define your sub-app logic in a separate file (e.g., sub_app.py)
quiz = Blueprint('quiz', __name__)

quiz_controller = QuizController()


@quiz.route('/')
def hello_world():
    return "Hello, World! Welcome to the quiz app!"


@quiz.route("/playQuiz", methods=['GET'])
def play_quiz():
    quiz_controller.play_quiz()
    return jsonify({"message": "Quiz ended"})


@quiz.route("/addQuizQuestion", methods=['POST'])
def add_quiz_question():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    id_category = data.get("id_category")
    question = data.get("question")
    option1 = data.get("option1")
    option2 = data.get("option2")
    option3 = data.get("option3")
    option4 = data.get("option4")
    correct = data.get("correct")

    if not id_category or not question or not option1 or not option2 or not option3 or not option4 or not correct:
        return jsonify({"error": "Incomplete data"}), 400

    try:
        quiz_controller.quiz_model.id_category = id_category
        quiz_controller.quiz_model.question = question
        quiz_controller.quiz_model.option1 = option1
        quiz_controller.quiz_model.option2 = option2
        quiz_controller.quiz_model.option3 = option3
        quiz_controller.quiz_model.option4 = option4
        quiz_controller.quiz_model.correct = int(correct)

        quiz_controller.quiz_model.save()
        return jsonify({"message": "Quiz question added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@quiz.route("/getAllQuizQuestions", methods=['GET'])
def get_all_quiz_questions():
    quiz_questions = quiz_controller.quiz_model.read()
    return jsonify({"quiz_questions": quiz_questions})