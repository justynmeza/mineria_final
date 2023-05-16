from flask import jsonify, request

from models.games import *

mod_games = Games()

class games_controller():

    def c_consult_games(self):
        query = mod_games.m_consult_games()
        return query
    
    def c_consult_game_by_id(self):
        query = mod_games.m_consult_game_by_id()
        return query
    
    def c_create_game(self):
        query = mod_games.m_create_game()
        return query
    
    def c_update_game(self):
        query = mod_games.m_update_game()
        return query
    
    def c_delete_game(self):
        query = mod_games.m_delete_game()
        return query