from flask import jsonify, request

from models.predict import *

mod_predict = Predict()

class Predict_controller():
    
    def c_predict(self):
        query = mod_predict.m_predict()
        return query