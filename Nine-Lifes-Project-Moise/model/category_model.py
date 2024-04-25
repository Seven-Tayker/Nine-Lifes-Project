import sqlite3
from .basemodel import AbstractBaseModel
from .constant import PATH_TO_DB
from model import createdb

createdb.databaseSetup()


class Category(AbstractBaseModel):
    TABLE_NAME = "Category"

    def init(self, id_category=None, category_name=None, nb_of_questions=None) -> None:
        super().init()
        self.id_category = id_category
        self.category_name = category_name
        self.nb_of_questions = nb_of_questions

    def save(self):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()
            if self.id_category:
                query = f"UPDATE {self.TABLE_NAME} SET category_name=?, nb_of_questions=? WHERE id_category=?"
                cursor.execute(query, (self.category_name, self.nb_of_questions, self.id_category))
            else:
                query = f"INSERT INTO {self.TABLE_NAME} (category_name, nb_of_questions) VALUES (?, ?)"
                cursor.execute(query, (self.category_name, self.nb_of_questions))
                self.id_category = cursor.lastrowid
        connection.commit()

    def read(self, id=None):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()
            if id:
                query = f"SELECT id_category, category_name, nb_of_questions FROM {self.TABLE_NAME} WHERE id_category=?"
                cursor.execute(query, (id,))
                result = cursor.fetchone()
                if result:
                    category = Category(id_category=result[0], category_name=result[1], nb_of_questions=result[2])
                    return category.toJSON()
                else:
                    return None
            else:
                query = f"SELECT id_category, category_name, nb_of_questions FROM {self.TABLE_NAME}"
                results = cursor.execute(query).fetchall()
                categories = []
                for result in results:
                    category = Category(id_category=result[0], category_name=result[1], nb_of_questions=result[2])
                    categories.append(category.toJSON())
                return categories

    def delete(self):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()
            if self.id_category:
                cursor.execute(f"DELETE FROM {self.TABLE_NAME} WHERE id_category=?", (self.id_category,))
            else:
                cursor.execute(f"DELETE FROM {self.TABLE_NAME}")
        self.id_category = None

    def toJSON(self):
        dictionary = {
            "id_category": self.id_category,
            "category_name": self.category_name,
            "nb_of_questions": self.nb_of_questions
        }
        return dictionary