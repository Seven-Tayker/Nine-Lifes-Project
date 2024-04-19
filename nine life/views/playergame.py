from flask import Blueprint, request
from controllers.player_game import *

player_game_view = Blueprint('player_game', __name__, url_prefix='/player-game')

@player_game_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        return get_all_player_games()
    else:
        submitted_data = request.get_json()
        player_id, game_id = submitted_data['player_id'], submitted_data['game_id']
        return save_player_game(player_id, game_id)

@player_game_view.route('/<id>', methods=['GET', 'PUT', 'DELETE'])
def get_or_update_or_delete(id_player_game):
    if request.method == 'GET':
        return get_player_game_by_id(id_player_game)
    elif request.method == 'PUT':
        submitted_data = request.get_json()
        player_id, game_id = submitted_data['player_id'], submitted_data['game_id']
        return update_player_game(id_player_game, player_id, game_id)
    elif request.method == 'DELETE':
        return delete_player_game(id_player_game)
          pass