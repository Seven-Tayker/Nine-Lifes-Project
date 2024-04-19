import os

# from models.game import Game
from ..models.game import Game

def get_all_games():
    return Game.read()

def get_game_with_id(id_game):
    return Game.read(id_game)

def save_game(nb_of_players,date, id_game=None):
    if id_game != None:
        game = get_game_with_id(id_game)
        game.nb_of_players, game.date = (
            nb_of_players, date)
    else:
        game = game(
            nb_of_players=nb_of_players,date=date
         )

    game.save()

    return game
    
def delete_game(id_game):
    game = get_game_with_id(id_game)
    game.delete()


