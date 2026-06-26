from flask import Flask
from flask_cors import CORS

from routes.banner import banner_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(banner_bp)

@app.route("/")
def home():
    return {
        "status": "ok",
        "message": "Zenkai Backend Running"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
