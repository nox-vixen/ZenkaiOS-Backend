from flask import Blueprint, jsonify

anime_bp = Blueprint("anime", __name__)

@anime_bp.route("/api/anime")
def anime():

    return jsonify({
        "message": "Anime route working"
    })
