from flask import Blueprint, request
from controller.playerGame_controller import *

playerGameView = Blueprint('playerGame', __name__, url_prefix='/playerGame')


@playerGameView.route('/')
def home():
    return "<center><h1>Welcome to the PLAYER_GAME VIEW</h1></center>"


@playerGameView.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = request.form
        if data['id_player'] and data['id_game']:
            playergame = save_playerGame(data['id_player'], data['id_game'])
            return playergame
        else:
            return "<center><h3> Enter all required informations </h3></center>"
    else:
        return "<center><h3>Fill the form</h3></center>"


@playerGameView.route('/getById', methods=['GET', 'POST'])
def getById():
    if request.method == 'POST':
        data = request.form
        playergame = get_playerGame_with_id(playerGame_id=data['id'])
        # print("\nid :"+data['id'])
        return playergame
    else:
        return "<center><h3> Enter the Id </h3></center>"


@playerGameView.route('/getAll', methods=['GET'])
def getAll():
    playergame = get_all_playerGames()
    return playergame


@playerGameView.route('/update', methods=['GET', 'PUT'])
def update():
    if request.method == 'PUT':
        data = request.form
        if data['id_player'] and data['id_game'] and data['id']:
            gam = get_playerGame_with_id(data['id'])
            if gam:
                playergame = update_playerGame(data['id'], data['id_player'], data['id_game'])
                return playergame
            return "<center><h3> Not found </h3></center>"
        else:
            return "<center><h3> Enter all required informations </h3></center>"
    else:
        return "<center><h3>Fill the form</h3></center>"


@playerGameView.route('/deleteById', methods=['GET', 'DELETE', 'POST'])
def deleteById():
    if request.method == 'DELETE':
        data = request.form
        if data['id']:
            gam = get_playerGame_with_id(data['id'])
            if gam:
                delete_playerGame_with_id(data['id'])
                return "<center><h3> Game with Id :" + data['id'] + " was successfully deleted </h3></center>"
            return "<center><h3> Not found </h3></center>"
        else:
            return "<center><h3> Enter the Id of the Game to be deleted </h3>"
    else:
        return "<center><h3> Incorrect Method </h3></center>"


@playerGameView.route('/deleteAll', methods=['GET', 'DELETE', 'POST'])
def deleteAll():
    if request.method == 'DELETE':
        delete_all()
        return "<center><h3> All the PLayer_Games were deleted successfully </h3></center>"
    else:
        return "<center><h3> Incorrect Method </h3></center>"
