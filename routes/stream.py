from flask import Blueprint, jsonify

from backend.moviebox_service import moviebox_service

stream_bp = Blueprint("stream", __name__)


@stream_bp.route("/api/moviebox/search/<path:title>")
def moviebox_search(title):

    result = moviebox_service.first_match(title)

    if result is None:

        return jsonify({
            "success": False,
            "message": "Anime not found"
        }), 404

    return jsonify({
        "success": True,
        "data": result
    })


from pathlib import Path
import inspect
from moviebox_api.v1 import TVSeriesDetails


@stream_bp.route("/debug/cache")
def debug_cache():

    folder = Path("cache/moviebox")

    return jsonify({
        "files": [
            file.name
            for file in folder.glob("*.json")
        ]
    })


@stream_bp.route("/debug/tv_signature")
def tv_signature():

    return jsonify({
        "signature": str(
            inspect.signature(
                TVSeriesDetails
            )
        )
    })
