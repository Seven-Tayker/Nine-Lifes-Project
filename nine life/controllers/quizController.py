import sqlite3

from models.quiz import *


class Quiz:
    pass


class QuizController:
    def __init__(self):
        self.quiz_model = Quiz()

    def play_quiz(self):
        lives = 9  # Number of lives for the player
        score = 0  # Player's score

        # Retrieve all quiz questions
        quiz_questions = self.quiz_model.read()

        for question in quiz_questions:
            print(question["question"])
            print("Options:")
            print("1. " + question["option1"])
            print("2. " + question["option2"])
            print("3. " + question["option3"])
            print("4. " + question["option4"])

            answer = input("Enter your answer (1-4): ")

            # Validate the answer
            if answer.isdigit() and 1 <= int(answer) <= 4:
                if int(answer) == question["correct"]:
                    print("Correct answer!")
                    score += 1
                else:
                    print("Incorrect answer!")
                    lives -= 1

                print("Score:", score)
                print("Lives:", lives)
                print()

                if lives == 0:
                    break
            else:
                print("Invalid input. Please enter a number between 1 and 4.")

        print("Quiz ended. Final score:", score)

    def add_quiz_question(self):
        id_category = input("Enter the category ID: ")
        question = input("Enter the question: ")
        option1 = input("Enter option 1: ")
        option2 = input("Enter option 2: ")
        option3 = input("Enter option 3: ")
        option4 = input("Enter option 4: ")
        correct = input("Enter the correct option number (1-4): ")

        # Validate the correct option
        if correct.isdigit() and 1 <= int(correct) <= 4:
            self.quiz_model.id_category = id_category
            self.quiz_model.question = question
            self.quiz_model.option1 = option1
            self.quiz_model.option2 = option2
            self.quiz_model.option3 = option3
            self.quiz_model.option4 = option4
            self.quiz_model.correct = int(correct)

            self.quiz_model.save()
            print("Quiz question added successfully!")
        else:
            print("Invalid input for the correct option. Please enter a number between 1 and 4.")

    def run(self):
        while True:
            print("1. Play Quiz")
            print("2. Add Quiz Question")
            print("3. Exit")

            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.add_quiz_question()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")


# Usage example
controller = QuizController()
controller.run()