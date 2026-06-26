from flask import Blueprint, jsonify, request

from backend.moviebox import moviebox

search_bp = Blueprint(
    "search",
    __name__
)


@search_bp.route("/api/search")
def search():

    keyword = request.args.get("q", "")

    if not keyword:

        return jsonify([])

    return jsonify(
        moviebox.search(keyword)
    )
