from flask import Blueprint, jsonify

from backend.moviebox import moviebox

search_bp = Blueprint("search", __name__)


@search_bp.route("/api/test")
def test():
    return jsonify(
        moviebox.test(
            "/wefeed-h5api-bff/search?keyword=one%20piece"
        )
    )
