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
    
    def c_all_genders(self):
        query = mod_games.m_all_genders()
        return query

    def c_all_consoles(self):
        query = mod_games.m_all_consoles()
        return query

    def c_best_5_game_sales(self):
        query = mod_games.m_best_5_game_sales()
        return query

    def c_best_game_north_america(self):
        query = mod_games.m_best_game_north_america()
        return query

    def c_best_game_europe(self):
        query = mod_games.m_best_game_europe()
        return query

    def c_best_game_japan(self):
        query = mod_games.m_best_game_japan()
        return query

    def c_best_game_rest_of_world(self):
        query = mod_games.m_best_game_rest_of_world()
        return query

    def c_best_game_global(self):
        query = mod_games.m_best_game_global()
        return query