import sqlite3
from base_model import AbstractBaseModel


class Category(AbstractBaseModel):
    def __init__(self, category_name=None):
        self.category_name = category_name

    def create(self):
        query = "INSERT INTO Category (category_name) VALUES (?);"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            cursor.execute(query, (self.category_name,))

    @staticmethod
    def read():
        query = "SELECT * FROM Category;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            results = cursor.execute(query).fetchall()
            categories = []
            for result in results:
                category = Category(category_name=result[1])
                categories.append(category)
        return categories

    def readById(self, i=None):
        query = "SELECT * FROM Category WHERE id_category=?;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()  
            result = cursor.execute(query, (i,)).fetchone()
        return result

    def update(self, i=None):
        if i is not None:
            query = "UPDATE Category SET category_name=? WHERE id_category=?;"
            with sqlite3.connect("NLG") as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.category_name, i))
            return
        return "No Id for the update"

    def deleteById(self, i=None):
        query = "DELETE FROM Category WHERE id_category=?;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            cursor.execute(query, (i,))

    @staticmethod
    def delete():
        query = "DELETE FROM Category;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            cursor.execute(query)