from flask import Flask, jsonify, request, Blueprint
from flask_cors import  cross_origin
from controllers.users_controller import *


con_user= User_controller()

users = Blueprint('users', __name__)

@users.route('/userslist', methods=['GET'])
@cross_origin()
def userslist():
    return con_user.c_consult_user()

@users.route('/user', methods=['GET', 'POST'])
@cross_origin()
def user_by_id():
    return con_user.c_consult_user_by_id()