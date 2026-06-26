from flask import Blueprint
from flask import jsonify
from flask import request

from backend.search_service import search_service


search_bp = Blueprint(
    "search",
    __name__
)


@search_bp.route("/api/search")
def search():

    keyword = request.args.get(
        "q",
        ""
    ).strip()

    if not keyword:
        return jsonify([])

    return jsonify(
        search_service.search(keyword)
    )
