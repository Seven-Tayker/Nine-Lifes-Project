import os
import sqlite3


def databaseSetup():
    DB = os.path.join(os.path.dirname(__file__), "NLG.sqlite")

    game_query = "CREATE TABLE IF NOT EXISTS Game (" \
                 "id_game integer PRIMARY KEY, " \
                 "nb_of_players integer, " \
                 "date DATETIME" \
                 ")"
    player_query = "CREATE TABLE IF NOT EXISTS Player (" \
                   "id_player text PRIMARY KEY," \
                   "player_name text," \
                   "email text," \
                   "rank int," \
                   "nb_game_played int," \
                   "nb_game_loosed int," \
                   "nb_game_won int " \
                   ")"
    category_query = "CREATE TABLE IF NOT EXISTS Category (" \
                     "id_category int AUTO_INCREMENT PRIMARY KEY," \
                     "category_name text," \
                     "nb_of_questions int" \
                     ")"
    playerGame_query = "CREATE TABLE IF NOT EXISTS PlayerGame(" \
                       "playerGame_id int AUTO_INCREMENT PRIMARY KEY," \
                       "id_player text," \
                       "id_game int," \
                       "FOREIGN KEY (id_player) REFERENCES Player(id_player)," \
                       "FOREIGN KEY (id_game) REFERENCES Game(id_game)" \
                       ")"
    quiz_query = "CREATE TABLE IF NOT EXISTS Quiz (" \
                 "id_quiz int AUTO_INCREMENT PRIMARY KEY," \
                 "id_category int," \
                 "question text," \
                 "option1 text," \
                 "option2 text," \
                 "option3 text," \
                 "option4 text," \
                 "correct text," \
                 "FOREIGN KEY (id_category) REFERENCES Category(id_category)" \
                 ")"

    with sqlite3.connect(DB) as connection:
        cursor = connection.cursor()
        for query in [game_query, player_query, category_query, playerGame_query, quiz_query]:
            cursor.execute(query)
    connection.commit()
    connection.close()
