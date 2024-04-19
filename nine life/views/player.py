from flask import Blueprint, request
from controllers.player import *

player_view = Blueprint('player', __name__, url_prefix='/player')

@player_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        return get_all_players()
    else:
        submitted_data = request.get_json()
        name, email = submitted_data['name'], submitted_data['email']
        return save_player(name, email)

@player_view.route('/<id>', methods=['GET', 'PUT', 'DELETE'])
def get_or_update_or_delete(id_player):
    if request.method == 'GET':
        return get_player_by_id(id_player)
    elif request.method == 'PUT':
        submitted_data = request.get_json()
        name, email = submitted_data['name'], submitted_data['email']
        return update_player(id_player, name, email)
    elif request.method == 'DELETE':
        return delete_player(id_player)
        pass