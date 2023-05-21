from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin
from functools import wraps
from config import *
from routes.users_route import users
from routes.games_route import games
from routes.predict_route import predict

app = Flask(__name__)
#CORS(app, resources={r"/*": {"origins": "*"}})
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(users)
app.register_blueprint(games)
app.register_blueprint(predict)

@app.route('/')
@cross_origin()  
def index():
    return render_template('index.html')

    
def pagina_no_encontrada(error):
    
    return "<h1>La pagina a la que intentas acceder no existe...</h1>"
    


if __name__=="__main__":
    app.register_error_handler(404 , pagina_no_encontrada)
    ##app.run(debug=True, host="0.0.0.0")
    app.run(debug=True)