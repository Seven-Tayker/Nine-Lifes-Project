from model.playerGame_model import PlayerGame


def save_playerGame(id_player, id_game):
    playergame = PlayerGame(id_player=id_player, id_game=id_game)
    playergame.save()
    return playergame.toJSON()


def get_all_playerGames():
    playergame = PlayerGame()
    return playergame.read()


def get_playerGame_with_id(playerGame_id, self=None):
    playergame = PlayerGame.read(self, id=playerGame_id)
    return playergame


def update_playerGame(id, id_player, id_game):
    playergame = PlayerGame(id, id_player, id_game)
    playergame.save()
    return playergame.toJSON()


def delete_playerGame_with_id(id):
    playergame = PlayerGame(playerGame_id=id)
    playergame.delete()
    return playergame.toJSON()


def delete_all():
    playergame = PlayerGame()
    playergame.delete()
    return True
