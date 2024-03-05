from flask import Flask
from flask_cors import CORS
from src.main.routes.app_routes import app_routes_bp
from src.main.routes.poke_routes import poke_routes_bp


app = Flask(__name__)
CORS(app)
app.config['MONGO_URI'] = 'mongodb://mongo-api:27017/poke_database'

app.register_blueprint(app_routes_bp)
app.register_blueprint(poke_routes_bp)

#docker run -d --name mongo-api --network net-api mongo --bind_ip_all
