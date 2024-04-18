from model.game_model import Game


def save_game(nb_of_players, date):
    game = Game(nb_of_players=nb_of_players, date=date)
    game.save()
    return game.toJSON()


def get_all_games():
    game = Game()
    return game.read()


def get_game_with_id(id_game, self=None):
    game = Game.read(self, id=id_game)
    return game


def update_game(id, nb_of_players, date):
    game = Game(id, nb_of_players, date)
    game.save()
    return game.toJSON()


def delete_game_with_id(id_game):
    game = Game(id_game=id_game)
    game.delete()
    return game.toJSON()


def delete_all():
    game = Game()
    game.delete()
    return True
