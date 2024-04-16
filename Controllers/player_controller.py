from model import player_model


def get_all_player(return_objects=False):
    objects = player_model.Player.read()

    if not return_objects:
        list_of_objects = [
            obj.toJSON() for obj in objects
        ]
        return list_of_objects
    return objects


def get_player_with_id(id):
    return player_model.Player.read(id).toJSON()


def save_player(username, email, password, id=None):
    if id is not None:
        # get subject with id
        player = get_player_with_id(id)
        player.username = username
        player.email = email
        player.password = password
    else:
        player = player_model.Player(username=username, email=email, password=password)

    player.save(player_id, category_id, difficulty_id, score, remaining_lives, start_time, end_time)

    return player.toJSON()


def delete_player(id):
    player = get_player_with_id(id)
    player.delete()
    return player.toJSON()



