import sqlite3

class PlayerGameModel:
    def __init__(self, player_id, game_id):
        self.player_id = player_id
        self.game_id = game_id

    def create(self):
        connection = sqlite3.connect("your_database.db")
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO PlayerGame (id_player, id_game)
            VALUES (?, ?)
            """,
            (self.player_id, self.game_id)
        )
        connection.commit()
        connection.close()

    @staticmethod
    def read():
        connection = sqlite3.connect("your_database.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM PlayerGame")
        rows = cursor.fetchall()
        connection.close()

        player_games = []
        for row in rows:
            player_game = PlayerGameModel(row[1], row[2])
            player_games.append(player_game)

        return player_games

    @staticmethod
    def read_by_player_id(player_id):
        connection = sqlite3.connect("your_database.db")
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT * FROM PlayerGame
            WHERE id_player = ?
            """,
            (player_id,)
        )
        rows = cursor.fetchall()
        connection.close()

        player_games = []
        for row in rows:
            player_game = PlayerGameModel(row[1], row[2])
            player_games.append(player_game)

        return player_games

    @staticmethod
    def read_by_game_id(game_id):
        connection = sqlite3.connect("your_database.db")
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT * FROM PlayerGame
            WHERE id_game = ?
            """,
            (game_id,)
        )
        rows = cursor.fetchall()
        connection.close()

        player_games = []
        for row in rows:
            player_game = PlayerGameModel(row[1], row[2])
            player_games.append(player_game)

        return player_games

    def delete(self):
        connection = sqlite3.connect("your_database.db")
        cursor = connection.cursor()
        cursor.execute(
            """
            DELETE FROM PlayerGame
            WHERE id_player = ? AND id_game = ?
            """,
            (self.player_id, self.game_id)
        )
        connection.commit()
        connection.close()