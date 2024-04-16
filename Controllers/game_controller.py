from ..model.game_model import QuizGame


def get_all_game(return_objects=False):
    objects = QuizGame.read()

    if not return_objects:
        list_of_objects = [
            obj.toJSON() for obj in objects
        ]
        return list_of_objects
    return objects


def get_game_with_id(id):
    return QuizGame.read(id).toJSON()


def save_game(player_id, category_id, difficulty_id, score, remaining_lives, start_time, end_time, id = None):
    if id is not None:
        game = get_game_with_id(id)
        game.player_id = player_id
        game.category_id = category_id
        game.difficulty_id = difficulty_id
    else:
        player = player_model.Player(username=username, email=email, password=password)

    player.save()

    return player.toJSON()
