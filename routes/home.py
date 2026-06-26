from flask import Blueprint, jsonify

from backend.moviebox import get_home

home_bp = Blueprint(
    "home",
    __name__
)


@home_bp.route("/api/home")
def home():

    return jsonify(
        get_home()
    )
