from flask import Blueprint, jsonify

from backend.home_service import home_service

home_bp = Blueprint(
    "home",
    __name__
)


@home_bp.route("/api/home")
def home():

    return jsonify(
        home_service.get_home()
    )
