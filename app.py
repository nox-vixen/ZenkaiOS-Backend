from flask import Flask, render_template
from flask_cors import CORS

from routes.anime import anime_bp
from routes.home import home_bp
from routes.search import search_bp
from routes.watch import watch_bp
from routes.details import details_bp
from routes.stream import stream_bp

from backend.anilist import get_trending_anime
from backend.cache_builder import build_cache

app = Flask(__name__)
CORS(app)

app.register_blueprint(anime_bp)
app.register_blueprint(home_bp)
app.register_blueprint(search_bp)
app.register_blueprint(watch_bp)
app.register_blueprint(details_bp)
app.register_blueprint(stream_bp)

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/watch/<int:anime_id>")
def watch(anime_id):
    return render_template(
        "watch.html",
        anime_id=anime_id
    )


@app.route("/debug/anilist")
def debug_anilist():
    return get_trending_anime(5)

@app.route("/build-cache")
def build_cache_route():

    build_cache()

    return {
        "status": "success",
        "message": "Cache rebuilt successfully."
    }

@app.route("/routes")
def show_routes():
    return {
        "routes": sorted(
            str(rule)
            for rule in app.url_map.iter_rules()
        )
    }

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
