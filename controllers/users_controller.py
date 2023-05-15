from flask import jsonify, request

from models.users import *

mod_user = User()

class User_controller():
    
    def c_consult_user(self):
        query = mod_user.m_consult_user()
        return query
    
    def c_consult_user_by_id(self):
        query = mod_user.m_consult_user_by_id()
        return query