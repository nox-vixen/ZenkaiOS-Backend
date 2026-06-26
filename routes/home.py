from flask import Blueprint
from flask import jsonify

home_bp = Blueprint(
    "home",
    __name__
)

@home_bp.route("/api/home")
def home():
    return jsonify({
        "status": "Rebuilding Home API"
    })
