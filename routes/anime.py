from flask import Blueprint, jsonify

from backend.anime_engine import anime_engine

anime_bp = Blueprint(
    "anime",
    __name__
)


@anime_bp.route("/api/anime/<int:anime_id>")
def anime(anime_id):

    return jsonify(

        anime_engine.build(anime_id)

    )
