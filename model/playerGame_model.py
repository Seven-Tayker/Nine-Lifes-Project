import sqlite3
from .basemodel import AbstractBaseModel
from .constant import PATH_TO_DB
from model import createdb

createdb.databaseSetup()


class PlayerGame(AbstractBaseModel):
    TABLE_NAME = "playerGame"

    def __init__(self, playerGame_id=None, id_player=None, id_game=None) -> None:
        super().__init__()
        self.playerGame_id = playerGame_id
        self.id_player = id_player
        self.id_game = id_game

    def save(self):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()
            if self.playerGame_id:
                query = f"UPDATE {self.TABLE_NAME} SET id_player=?, id_game=? WHERE playerGame_id=?"
                cursor.execute(query, (self.id_player, self.id_game, self.playerGame_id))
            else:
                query = f"INSERT INTO {self.TABLE_NAME} (id_player, id_game) VALUES (?, ?)"
                cursor.execute(query, (self.id_player, self.id_game))
                # get the newly created record's IDs
                # id = cursor.execute(f"SELECT MAX(playerGame_id) FROM {self.TABLE_NAME}").fetchone()[0]
                # self.id = id
                self.playerGame_id = cursor.lastrowid
        connection.commit()

    def read(self, id=None):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()
            if id:
                query = f"SELECT id_player, id_game date FROM Game WHERE playerGame_id="+id
                cursor.execute(query)
                result = cursor.fetchone()
                # param1 = result[]
                # param2 = result[2]
                # param3 = result[0]
                playergame = __class__(playerGame_id=result[0], id_player=result[1], id_game=result[2])
                # response = JSONResponse(status=200, content_type="application/json", data=game)
                return playergame.toJSON2()
            else:
                query = f"SELECT playerGame_id, id_player, id_game FROM playerGame"
                results = cursor.execute(query).fetchall()
                playergames = []
                for result in results:
                    playergame = __class__(playerGame_id=result[0], id_player=result[1], id_game=result[2])
                    playergames.append(playergame.toJSON2())
                return playergames

    def delete(self):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()
            if self.playerGame_id:
                cursor.execute(f"DELETE FROM {self.TABLE_NAME} WHERE playerGame_id=?", self.playerGame_id)
            else:
                cursor.execute(f"DELETE FROM {self.TABLE_NAME}")
        self.playerGame_id = None

    def toJSON(self):
        dictionary = {
            "Player Id ": self.id_player,
            "Game Id ": self.id_game
        }
        return dictionary

    def toJSON2(self):
        dictionary = {
            "Player_Game Id ": self.playerGame_id,
            "Player Id ": self.id_player,
            "Game Id ": self.id_game
        }
        return dictionary
