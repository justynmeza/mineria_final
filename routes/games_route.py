from flask import Flask, jsonify, request, Blueprint
from flask_cors import  cross_origin
from controllers.games_controller import *

con_games = games_controller()

games = Blueprint('games', __name__)

@games.route('/gameslist', methods=['GET'])
@cross_origin()
def gamelist():
    return con_games.c_consult_games()

@games.route('/game', methods=['GET', 'POST'])
@cross_origin()
def game_by_id():
    return con_games.c_consult_game_by_id()

@games.route('/game/create', methods=['POST'])
@cross_origin()
def game_create():
    return con_games.c_create_game()

@games.route('/game/update', methods=['PUT', 'POST'])
@cross_origin()
def game_update():
    return con_games.c_update_game()

@games.route('/game/delete', methods=['DELETE', 'POST'])
@cross_origin()
def game_delete():
    return con_games.c_delete_game()