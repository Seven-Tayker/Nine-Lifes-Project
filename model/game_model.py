import sqlite3
from .basemodel import AbstractBaseModel
from model import createdb

createdb.databaseSetup()


class Game(AbstractBaseModel):
    TABLE_NAME = "Game"

    def __init__(self, id_game=None, nb_of_players=None, date=None) -> None:
        super().__init__()
        self.id_game = id_game
        self.nb_of_players = nb_of_players
        self.date = date

    def save(self):
        with sqlite3.connect("NLG.sqlite") as connection:
            cursor = connection.cursor()
            if self.id_game:
                query = f"UPDATE {self.TABLE_NAME} SET nb_of_players=?, date=? WHERE id_game=?"
                cursor.execute(query, (self.nb_of_players, self.date, self.id_game))
            else:
                query = f"INSERT INTO {self.TABLE_NAME} (nb_of_players, date) VALUES (?, ?)"
                cursor.execute(query, (self.nb_of_players, self.date))
                # get the newly created record's id
                id = cursor.execute(f"SELECT MAX(id_game) FROM {self.TABLE_NAME}").fetchone()[0]
                self.id = id
        connection.commit()

    def read(self, id=None):
        with sqlite3.connect("NLG.sqlite") as connection:
            cursor = connection.cursor()
            if id:
                query = f"SELECT id_game, nb_of_players, date FROM Game WHERE id_game="+id
                cursor.execute(query)
                result = cursor.fetchone()
                game = __class__(id_game=result[0], nb_of_players=result[1], date=result[2])
                # response = JSONResponse(status=200, content_type="application/json", data=game)
                return game
            else:
                query = f"SELECT id_game, nb_of_players, date FROM Game"
                results = cursor.execute(query).fetchall()
                games = []
                for result in results:
                    game = __class__(id_game=result[0], nb_of_players=result[1], date=result[2])
                    games.append(game.toJSON2())
                return games

    def delete(self):
        with sqlite3.connect("NLG.sqlite") as connection:
            cursor = connection.cursor()
            if self.id_game:
                cursor.execute(f"DELETE FROM {self.TABLE_NAME} WHERE id=?", self.id)
            else:
                cursor.execute(f"DELETE FROM {self.TABLE_NAME}")
        self.id_game = None

    def toJSON(self):
        dictionary = {
            "Number of players ": self.nb_of_players,
            "Date ": self.date
        }
        return dictionary

    def toJSON2(self):
        dictionary = {
            "Number of players ": self.nb_of_players,
            "Date ": self.date,
            "id ": self.id_game
        }
        return dictionary
