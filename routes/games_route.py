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

@games.route('/allgenders', methods=['GET'])
@cross_origin()
def all_genders():
    return con_games.c_all_genders()

@games.route('/allconsoles', methods=['GET'])
@cross_origin()
def all_consoles():
    return con_games.c_all_consoles()

@games.route('/best5', methods=['GET'])
@cross_origin()
def best_5_game_sales():
    return con_games.c_best_5_game_sales()

@games.route('/bestnorthamerica', methods=['GET'])
@cross_origin()
def best_game_nort_america():
    return con_games.c_best_game_north_america()

@games.route('/besteurope', methods=['GET'])
@cross_origin()
def best_game_europe():
    return con_games.c_best_game_europe()

@games.route('/bestjapan', methods=['GET'])
@cross_origin()
def best_game_japan():
    return con_games.c_best_game_japan()

@games.route('/bestrestofworld', methods=['GET'])
@cross_origin()
def best_game_rest_of_world():
    return con_games.c_best_game_rest_of_world()

@games.route('/bestglobal', methods=['GET'])
@cross_origin()
def best_game_global():
    return con_games.c_best_game_global()