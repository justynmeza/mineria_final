from flask import Flask, jsonify, request, Blueprint
from flask_cors import  cross_origin
from controllers.predict_controller import *

con_predict = Predict_controller()

predict = Blueprint('predict', __name__)

@predict.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict_data():
    return con_predict.c_predict()