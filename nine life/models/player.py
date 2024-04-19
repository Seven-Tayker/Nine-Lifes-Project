import sqlite3

class Player:
    def __init__(self, id_player=None, player_name=None, email=None, rank=None, nb_game_played=None, nb_game_loosed=None, nb_game_won=None):
        self.id_player = id_player
        self.player_name = player_name
        self.email = email
        self.rank = rank
        self.nb_game_played = nb_game_played
        self.nb_game_loosed = nb_game_loosed
        self.nb_game_won = nb_game_won

    def create(self):
        query = "INSERT INTO Player (id_player, player_name, email, rank, nb_game_played, nb_game_loosed, nb_game_won) VALUES (?, ?, ?, ?, ?, ?, ?);"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            cursor.execute(query, (self.id_player, self.player_name, self.email, self.rank, self.nb_game_played, self.nb_game_loosed, self.nb_game_won))

    def read(self):
        query = "SELECT * FROM Player;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            results = cursor.execute(query).fetchall()
            players = []
            for result in results:
                player = Player(id_player=result[0], player_name=result[1], email=result[2], rank=result[3], nb_game_played=result[4], nb_game_loosed=result[5], nb_game_won=result[6])
                players.append(player)
        return players

    def readById(self, id_player):
        query = "SELECT * FROM Player WHERE id_player=?;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            result = cursor.execute(query, (id_player,)).fetchone()
            if result:
                return Player(id_player=result[0], player_name=result[1], email=result[2], rank=result[3], nb_game_played=result[4], nb_game_loosed=result[5], nb_game_won=result[6])
            else:
                return None

    def update(self, id_player):
        query = "UPDATE Player SET player_name=?, email=?, rank=?, nb_game_played=?, nb_game_loosed=?, nb_game_won=? WHERE id_player=?;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            cursor.execute(query, (self.player_name, self.email, self.rank, self.nb_game_played, self.nb_game_loosed, self.nb_game_won, id_player))

    def deleteById(self, id_player):
        query = "DELETE FROM Player WHERE id_player=?;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            cursor.execute(query, (id_player,))

    def delete(self):
        query = "DELETE FROM Player;"
        with sqlite3.connect("NLG") as connection:
            cursor = connection.cursor()
            cursor.execute(query)