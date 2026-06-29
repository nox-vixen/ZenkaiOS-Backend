from flask import Blueprint, jsonify

from backend.moviebox_service import moviebox_service

stream_bp = Blueprint("stream", __name__)


@stream_bp.route("/debug/moviebox")
def debug_moviebox():

    result = moviebox_service.search("One Piece")

    return jsonify(result.model_dump())
