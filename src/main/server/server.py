from flask import Flask
from flask_cors import CORS
from src.main.routes.app_routes import app_routes_bp
from src.main.routes.poke_routes import poke_routes_bp


app = Flask(__name__)
CORS(app)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/'

app.register_blueprint(app_routes_bp)
app.register_blueprint(poke_routes_bp)