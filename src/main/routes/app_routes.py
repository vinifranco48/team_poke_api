from flask import Blueprint, jsonify

app_routes_bp = Blueprint('app_routes', __name__)

@app_routes_bp.route('/', methods={'GET'})
def home():
    return jsonify({
        'resp':'ok'
    })
