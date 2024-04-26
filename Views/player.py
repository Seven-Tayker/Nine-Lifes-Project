from flask import Blueprint, request

from Controllers.player_controller import *

player = Blueprint('player', __name__, url_prefix='/player')

@player_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        return get_all_game()
    else:
        submitted_data = request.POST

        nb_of_players, date = (
            submitted_data['nb_of_players'], submitted_data['date'], 

        )

        return save_player(nb_of_players, date)
    
@player.route('/<id>', methods=['GET', 'POST'])
def get_or_update_instance(id_player):
    if request.method == 'GET':
        return get_player_with_id(id_player )
    pass