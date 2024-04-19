import os

from models.playerGame import PlayerGameModel


def get_all_playerGames():
    return PlayerGameModel.read()


def get_playerGame_with_id(id_game):
    return PlayerGameModel.read(id_game)


def save_playerGame(player_id, game_id):
    if game_id != None:
       player_id = player_id

       playerGame.player_id = (player_id)
    else:
        playerGame = playerGame(
            player_id
        )

    playerGame.save()

    return playerGame


def delete_playerGame(id_game):
    playerGame = get_playerGame_with_id(id_game)
    playerGame.delete()