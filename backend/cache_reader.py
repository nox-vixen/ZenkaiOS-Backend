import json
import os

CACHE_FILE = "cache/anime_cache.json"


def read_cache():

    if not os.path.exists(CACHE_FILE):
        return None

    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
