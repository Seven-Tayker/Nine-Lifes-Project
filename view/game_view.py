from flask import Blueprint, request
from controller.game_controller import *

# from middleware.Responses import JSONResponse
# , instance_not_found_response

gameView = Blueprint('game', __name__, url_prefix='/game')


@gameView.route('/')
def home():
    return "<center><h1>Welcome to the GAME VIEW</h1></center>"


@gameView.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = request.form
        if data['nb_of_players'] and data['date']:
            game = save_game(data['nb_of_players'], data['date'])
            # response = JSONResponse(status=200, content_type="application/json", data=game)
            return game
        else:
            return "<center><h3> Enter all required informations </h3></center>"
    else:
        return "<center><h3>Fill the form</h3></center>"


@gameView.route('/getById', methods=['GET', 'POST'])
def getById():
    if request.method == 'POST':
        data = request.form
        game = get_game_with_id(id_game=data['id'])
        # print("\nid :"+data['id'])
        return game
    else:
        return "<center><h3> Enter the Id </h3></center>"


@gameView.route('/getAll', methods=['GET'])
def getAll():
    game = get_all_games()
    return game


@gameView.route('/update', methods=['GET', 'PUT'])
def update():
    if request.method == 'PUT':
        data = request.form
        if data['nb_of_players'] and data['date'] and data['id']:
            gam = get_game_with_id(data['id'])
            if gam:
                game = update_game(data['id'], data['nb_of_players'], data['date'])
                return game
            return "<center><h3> Not found </h3></center>"
        else:
            return "<center><h3> Enter all required informations </h3></center>"
    else:
        return "<center><h3>Fill the form</h3></center>"


@gameView.route('/deleteById', methods=['GET', 'DELETE', 'POST'])
def deleteById():
    if request.method == 'DELETE':
        data = request.form
        if data['id']:
            gam = get_game_with_id(data['id'])
            if gam:
                delete_game_with_id(data['id'])
                return "<center><h3>PLayer_Game with Id :" + data['id'] + " was successfully deleted </h3></center>"
            return "<center><h3> Not found </h3></center>"
        else:
            return "<center><h3> Enter the Id of the Game to be deleted </h3>"
    else:
        return "<center><h3> Incorrect Method </h3></center>"


@gameView.route('/deleteAll', methods=['GET', 'DELETE', 'POST'])
def deleteAll():
    if request.method == 'DELETE':
        delete_all()
        return "<center><h3> All the Player_Games were deleted successfully </h3></center>"
    else:
        return "<center><h3> Incorrect Method </h3></center>"
