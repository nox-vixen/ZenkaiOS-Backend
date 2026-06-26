from flask import Blueprint
from flask import jsonify

anime_bp = Blueprint(
    "anime",
    __name__
)

@anime_bp.route("/api/anime")
def anime():
    return jsonify({
        "status": "Anime API rebuilding"
    })
