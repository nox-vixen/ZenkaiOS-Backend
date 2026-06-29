from flask import Blueprint
from flask import render_template

details_bp = Blueprint(
    "details",
    __name__
)

@details_bp.route("/details/<int:anime_id>")
def details(anime_id):

    return render_template(
        "details.html",
        anime_id=anime_id
    )
