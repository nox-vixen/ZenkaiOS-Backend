import json
import os

from backend.anilist import get_anime, get_trending_anime

CACHE_FILE = "cache/anime_cache.json"


def build_cache():

    data = {

        "featured": get_trending_anime(5),

        "trending": get_anime(["TRENDING_DESC"], 20),

        "popular": get_anime(["POPULARITY_DESC"], 20),

        "top_rated": get_anime(["SCORE_DESC"], 20),

        "new": get_anime(["START_DATE_DESC"], 20),

        "favorites": get_anime(["FAVOURITES_DESC"], 20)

    }

    os.makedirs("cache", exist_ok=True)

    with open(CACHE_FILE, "w", encoding="utf-8") as f:

        json.dump(data, f, ensure_ascii=False, indent=4)

    return data
