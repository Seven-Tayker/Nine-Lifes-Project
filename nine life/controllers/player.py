import os

from models.player import Player


def get_all_players():
    return Player.read()


def get_player_with_id(id_game):
    return Player.read(id_game)


def save_player( id=None, username, email, password):
    if id != None:
        player = get_player_with_id(id)
        player.username, player.email, player.password = (
            username, email, password)
    else:
        player = player(
            username=email, email=email, password=password
        )

    player.save()

    return player


def delete_player(id_player):
    player = get_player_with_id(id_player)
    player.delete()