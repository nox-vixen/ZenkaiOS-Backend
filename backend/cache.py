import json
import os

CACHE_FILE = "cache/anime_cache.json"


def load_cache():

    if not os.path.exists(CACHE_FILE):
        return {}

    try:
        with open(
            CACHE_FILE,
            "r",
            encoding="utf-8"
        ) as f:
            return json.load(f)

    except Exception:
        return {}


def save_cache(cache):

    with open(
        CACHE_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            cache,
            f,
            indent=4,
            ensure_ascii=False
        )


def get(title):

    cache = load_cache()

    return cache.get(title)


def exists(title):

    cache = load_cache()

    return title in cache


def put(title, data):

    cache = load_cache()

    cache[title] = data

    save_cache(cache)


def all():

    return load_cache()


def clear():

    save_cache({})
