from flask import Blueprint, jsonify

from backend.moviebox import moviebox

anime_bp = Blueprint(
    "anime",
    __name__
)


@anime_bp.route("/api/anime")
def anime():

    data = moviebox.home()

    anime = []

    for section in data["data"]["operatingList"]:

        title = section.get("title", "").lower()

        if "anime" not in title:
            continue

        for subject in section.get("subjects", []):

            anime.append({

                "title": subject.get("title"),

                "image": subject.get("cover", {}).get("url"),

                "rating": subject.get("imdbRatingValue"),

                "year": subject.get("releaseDate")

            })

    return jsonify(anime)
