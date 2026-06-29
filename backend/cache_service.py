from pathlib import Path
import json

CACHE_DIR = Path("cache/moviebox")

CACHE_DIR.mkdir(
parents=True,
exist_ok=True
)

class CacheService:

def load(self, key):

    file = CACHE_DIR / f"{key}.json"

    if not file.exists():
        return None

    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)

def save(self, key, data):

    file = CACHE_DIR / f"{key}.json"

    with open(file, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )

cache_service = CacheService()
