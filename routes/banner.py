from flask import Blueprint, jsonify
import requests

banner_bp = Blueprint("banner", __name__)

@banner_bp.route("/api/banner")
def banner():

    try:
        r = requests.get(
            "https://api.jikan.moe/v4/top/anime",
            timeout=15
        )

        data = r.json()

        banners = []

        for anime in data["data"][:5]:
            banners.append({
                "title": anime["title"],
                "image": anime["images"]["jpg"]["large_image_url"],
                "synopsis": anime.get("synopsis", "")[:200]
            })

        return jsonify(banners)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500
