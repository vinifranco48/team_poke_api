from flask import Flask
from flask_cors import CORS
from src.main.routes.app_routes import app_routes_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(app_routes_bp)
