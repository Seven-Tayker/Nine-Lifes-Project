import sqlite3
from base_model import AbstractBaseModel


class QuizModel(AbstractBaseModel):
    def __init__(self, id_category=None, question=None, option1=None, option2=None, option3=None, option4=None, correct_answer=None):
        self.id_category = id_category
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.correct_answer = correct_answer

    def create(self):
        query = "INSERT INTO Quiz (id_category, question, option1, option2, option3, option4, correct) VALUES (?, ?, ?, ?, ?, ?, ?);"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            cursor.execute(query, (self.id_category, self.question, self.option1, self.option2, self.option3, self.option4, self.correct_answer))

    def read(self):
        query = "SELECT * FROM Quiz;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            results = cursor.execute(query).fetchall()
            display = []
            for result in results:
                quiz = QuizModel(id_category=result[1], question=result[2], option1=result[3], option2=result[4], option3=result[5], option4=result[6], correct_answer=result[7])
                display.append(quiz)
        return display

    def readById(self, i=None):
        query = "SELECT * FROM Quiz WHERE id_quiz=?;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            result = cursor.execute(query, (i,)).fetchone()
        return result

    def update(self, i=None):
        if i is not None:
            query = "UPDATE Quiz SET id_category=?, question=?, option1=?, option2=?, option3=?, option4=?, correct=? WHERE id_quiz=?;"
            with sqlite3.connect("NLG") as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.id_category, self.question, self.option1, self.option2, self.option3, self.option4, self.correct_answer, i))
            return
        return "No Id for the update"

    def deleteById(self, i=None):
        query = "DELETE FROM Quiz WHERE id_quiz=?;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            cursor.execute(query, (i,))

    def delete(self):
        query = "DELETE FROM Quiz;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            cursor.execute(query)