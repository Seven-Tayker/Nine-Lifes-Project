import sqlite3
from .basemodel import AbstractBaseModel
from .constant import PATH_TO_DB
from model import createdb


createdb.databaseSetup()


class Quiz(AbstractBaseModel):
    TABLE_NAME = "Quiz"

    def init(self, id_quiz=None, id_category=None, question=None, option1=None, option2=None, option3=None,
             option4=None, correct=None):
        super().init()
        self.id_quiz = id_quiz
        self.id_category = id_category
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.correct = correct

    def save(self):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()
            if self.id_quiz:
                query = f"UPDATE {self.TABLE_NAME} SET id_category=?, question=?, option1=?, option2=?, " \
                        f"option3=?, option4=?, correct=? WHERE id_quiz=?"
                cursor.execute(query, (
                    self.id_category, self.question, self.option1, self.option2, self.option3, self.option4,
                    self.correct, self.id_quiz))
            else:
                query = f"INSERT INTO {self.TABLE_NAME} (id_category, question, option1, option2, option3, " \
                        f"option4, correct) VALUES (?, ?, ?, ?, ?, ?, ?)"
                cursor.execute(query, (
                    self.id_category, self.question, self.option1, self.option2, self.option3, self.option4,
                    self.correct))
                self.id_quiz = cursor.lastrowid
        connection.commit()

    def read(self, id=None):
        with sqlite3.connect(PATH_TO_DB) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            if id:
                query = f"SELECT * FROM {self.TABLE_NAME} WHERE id_quiz=?"
                cursor.execute(query, (id,))
                result = cursor.fetchone()
                if result:
                    quiz = Quiz(id_quiz=result["id_quiz"], id_category=result["id_category"],
                                question=result["question"], option1=result["option1"], option2=result["option2"],
                                option3=result["option3"], option4=result["option4"], correct=result["correct"])
                    return quiz.toJSON()
                else:
                    return None
            else:
                query = f"SELECT * FROM {self.TABLE_NAME}"
                results = cursor.execute(query).fetchall()
                quizzes = []
                for result in results:
                    quiz = Quiz(id_quiz=result["id_quiz"], id_category=result["id_category"],
                                question=result["question"], option1=result["option1"], option2=result["option2"],
                                option3=result["option3"], option4=result["option4"], correct=result["correct"])
                    quizzes.append(quiz.toJSON())
                return quizzes

    def delete(self):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()
            if self.id_quiz:
                cursor.execute(f"DELETE FROM {self.TABLE_NAME} WHERE id_quiz=?", (self.id_quiz,))
            else:
                cursor.execute(f"DELETE FROM {self.TABLE_NAME}")
        self.id_quiz = None

    def toJSON(self):
        dictionary = {
            "id_quiz": self.id_quiz,
            "id_category": self.id_category,
            "question": self.question,
            "option1": self.option1,
            "option2": self.option2,
            "option3": self.option3,
            "option4": self.option4,
            "correct": self.correct
        }
        return dictionary