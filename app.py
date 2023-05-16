from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from functools import wraps
from config import *
from routes.users_route import users
from routes.games_route import games

app = Flask(__name__)
#CORS(app, resources={r"/*": {"origins": "*"}})
cors = CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5000"}})

app.register_blueprint(users)
app.register_blueprint(games)

@app.route('/')
@cross_origin()  
def index():
    return jsonify({'message': 'welcome to games sales api'})

    
def pagina_no_encontrada(error):
    
    return "<h1>La pagina a la que intentas acceder no existe...</h1>"
    


if __name__=="__main__":
    app.register_error_handler(404 , pagina_no_encontrada)
    ##app.run(debug=True, host="0.0.0.0")
    app.run(port=5000, debug=True)