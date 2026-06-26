import requests
from flask import Response
from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    Response
)
from flask import Flask, jsonify, render_template
from flask_cors import CORS
import asyncio
import json
import os
from moviebox_client import moviebox_get

app = Flask(__name__)
CORS(app)

CACHE_FILE = "cache/anime_cache.json"


def load_cache():

    if not os.path.exists(CACHE_FILE):

        return {}

    try:

        with open(CACHE_FILE, "r") as f:

            return json.load(f)

    except Exception:

        return {}


def save_cache(data):

    with open(CACHE_FILE, "w") as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


def get_cached_anime(title):

    cache = load_cache()

    return cache.get(title)


def cache_anime(title, anime):

    cache = load_cache()

    cache[title] = anime

    save_cache(cache)

def get_anime(title):

    cached = get_cached_anime(title)

    if cached:

        print("[CACHE] Found:", title)

        return cached

    print("[CACHE MISS]", title)

    try:

        raw = asyncio.run(
            moviebox_get(
                f"/search?keyword={title}"
            )
        )

        return raw

    except Exception as e:

        print("MOVIEBOX SEARCH ERROR:", e)

        return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/anime")
def anime_page():
    return render_template("home-anime.html")

@app.route("/mylist")
def mylist():
    return render_template("home-mylist.html")

@app.route("/profile")
def profile():
    return render_template("home-profile.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

def get_jikan_image(title):

    try:

        clean_title = (
            title
            .replace("[Hindi]", "")
            .replace("[English]", "")
            .strip()
        )

        url = (
            "https://api.jikan.moe/v4/anime"
            f"?q={clean_title}&limit=1"
        )

        r = requests.get(url, timeout=10)

        data = r.json()

        if data.get("data"):

            return data["data"][0]["images"]["jpg"]["large_image_url"]

    except Exception as e:

        print("JIKAN ERROR:", e)

    return None

@app.route("/api/anime")
def anime():

    try:

        raw = asyncio.run(
            moviebox_get(
                "/wefeed-h5api-bff/home?host=moviebox.ph"
            )
        )

        text = raw["text"]

        parsed = json.loads(text)

        anime_list = []

        for section in parsed["data"]["operatingList"]:

            print("\n===================")
            print("TITLE:", section.get("title"))
            print("TYPE:", section.get("type"))
            print("SUBJECT COUNT:",
                  len(section.get("subjects", [])))

            if (
                section.get("type") == "SUBJECTS_MOVIE"
                and any(
                    keyword in section.get("title", "")
                    for keyword in [
                        "Anime",
                        "Animation",
                        "Top Anime"
                    ]
                )
            ):

                for subject in section.get("subjects", []):
                    with open("sample_anime.json", "w", encoding="utf-8") as f:
    json.dump(subject, f, indent=4, ensure_ascii=False)

                    print("Saved sample_anime.json")

                    break
                break
                    print(
    subject.get("title"),
    subject.get("cover", {}).get("url", "")
)
                    title = subject.get("title", "Unknown")

                    jikan_image = get_jikan_image(title)

                    anime_list.append({
    "title": title,
    "image": jikan_image,
    "rating": subject.get("imdbRatingValue", "N/A"),
    "year": subject.get("releaseDate", "")[:4],
    "episodes": "Anime",
    "tags": subject.get("genre", "").split(",")
})
        print("TOTAL ANIME =", len(anime_list))

        return jsonify(anime_list)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500
@app.route("/api/home")
def home_api():

    anime_data = asyncio.run(
        moviebox_get(
            "/wefeed-h5api-bff/home?host=moviebox.ph"
        )
    )

    parsed = json.loads(
        anime_data["text"]
    )

    return jsonify(parsed)

@app.route("/img")
def image_proxy():

    url = request.args.get("url")

    if not url:
        return "No URL", 400

    try:

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        print("STATUS =", r.status_code)
        print("CONTENT TYPE =", r.headers.get("Content-Type"))

        return Response(
            r.content,
            mimetype="image/jpeg"
        )

    except Exception as e:
        print("IMAGE ERROR =", e)
        return str(e), 500
@app.route("/api/banner")
def banner():

    try:

        r = requests.get(
            "https://api.jikan.moe/v4/top/anime"
        )

        data = r.json()

        banners = []

        for anime in data["data"][:5]:

            banners.append({
                "title": anime["title"],
                "image": anime["images"]["jpg"]["large_image_url"],
                "synopsis": anime.get("synopsis", "")[:150]
            })

        return jsonify(banners)

    except Exception as e:

        return jsonify({
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
