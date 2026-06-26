from flask import Blueprint, jsonify

from backend.banner import get_banner

banner_bp = Blueprint(
    "banner",
    __name__
)


@banner_bp.route("/api/banner")
def banner():

    return jsonify(
        get_banner()
    )
