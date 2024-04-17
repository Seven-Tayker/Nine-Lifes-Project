from flask import Blueprint, request

from Controllers.game_controller import *

game_view = Blueprint('game', __name__, url_prefix='/game')

@game_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        return get_all_game()
    else:
        submitted_data = request.POST

        nb_of_players, date = (
            submitted_data['nb_of_players'], submitted_data['date'], 

        )

        return save_game(nb_of_players, date)
    
@game_view.route('/<id>', methods=['GET', 'POST'])
def get_or_update_instance(id_game):
    if request.method == 'GET':
        return get_game_with_id(id_game)
    pass