from flask import Blueprint, render_template

watch_bp = Blueprint("watch", __name__)

@watch_bp.route("/watch/<int:anime_id>")
def watch(anime_id):
    return render_template("watch.html", anime_id=anime_id)
