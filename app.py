
from flask import Flask
from flask_cors import CORS

from routes.banner import banner_bp
from routes.anime import anime_bp
from routes.home import home_bp
from routes.search import search_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(banner_bp)
app.register_blueprint(anime_bp)
app.register_blueprint(home_bp)
app.register_blueprint(search_bp)

@app.route("/")
def home():
    return {
        "status": "ok",
        "message": "Zenkai Backend Running"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

@app.route("/debug/v1")
def debug_v1():
    from moviebox_api import v1

    return {
        "members": dir(v1)
    }
