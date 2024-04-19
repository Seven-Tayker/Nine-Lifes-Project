# from base_model import AbstractBaseModel
# from config.DataSource import DataSource

class Quiz:
    TABLE_NAME = "Quiz"

    def __init__(self, id_category=None, question=None, option1=None, option2=None, option3=None, option4=None,
                 correct=None):
        self.id_category = id_category
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.correct = correct
        self.ds = DataSource()

    def update_quiz(self, id_quiz, id_category):
        # update quiz if it exists
        query = f"UPDATE {self.__class__.TABLE_NAME} SET id_category=%s, question=%s, option1=%s, option2=%s, option3=%s, option4=%s, correct=%s WHERE id_quiz=%s"
        self.ds.execute(query, (
        id_category, self.question, self.option1, self.option2, self.option3, self.option4, self.correct, id_quiz,))

    def save(self):
        # save into database
        query = f"INSERT INTO {self.__class__.TABLE_NAME} (id_category, question, option1, option2, option3, option4, correct) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        self.ds.execute(query, (
        self.id_category, self.question, self.option1, self.option2, self.option3, self.option4, self.correct,))

    def save_multiple_quiz(self, data=[]):
        # save into database
        query = f"INSERT INTO {self.__class__.TABLE_NAME} (id_category, question, option1, option2, option3, option4, correct) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        self.ds.executemany(query, data)

    def read(self, id_quiz=None):
        if id_quiz:
            query = f"SELECT * FROM Quiz WHERE id_quiz=%s"
            result = self.ds.execute(query, (id_quiz,))
            return result
        else:
            query = f"SELECT * FROM Quiz"
            results = self.ds.execute(query)
            quizzes = []
            for result in results:
                quizzes.append(result)
            return quizzes
