from flask import Blueprint, jsonify, request
from backend.moviebox_service import moviebox

search_bp = Blueprint("search", __name__)


@search_bp.route("/api/search")
def search():

    keyword = request.args.get("q", "")

    if not keyword:
        return jsonify([])

    results = moviebox.search(keyword)

    anime = []

    for item in results.items:

        anime.append({
            "id": item.subjectId,
            "title": item.title,
            "description": item.description,
            "year": str(item.releaseDate),
            "duration": item.duration,
            "genres": item.genre,
            "image": str(item.cover.url)
        })

    return jsonify(anime)
