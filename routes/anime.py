from flask import Blueprint, jsonify

from backend.moviebox import get_home

anime_bp = Blueprint(
    "anime",
    __name__
)


@anime_bp.route("/api/anime")
def anime():

    data = get_home()

    return jsonify(data)
