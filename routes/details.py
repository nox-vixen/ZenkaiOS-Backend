from flask import Blueprint
from flask import render_template
from flask import jsonify

from backend.anilist import (
    get_anime_details,
    get_anime_characters
)

details_bp = Blueprint(
    "details",
    __name__
)

@details_bp.route("/details/<int:anime_id>")
def details_page(anime_id):

    return render_template(
        "details.html",
        anime_id=anime_id
    )

@details_bp.route("/api/details/<int:anime_id>")
def details_api(anime_id):

    return jsonify(
        get_anime_details(anime_id)
    )


@details_bp.route("/api/details/<int:anime_id>/characters")
def characters_api(anime_id):

    return jsonify(

        get_anime_characters(anime_id)

    )
