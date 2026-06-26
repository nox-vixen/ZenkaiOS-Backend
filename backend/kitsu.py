import requests

BASE_URL = "https://kitsu.io/api/edge/anime"

def search(title):
    try:

        r = requests.get(
            BASE_URL,
            params={
                "filter[text]": title,
                "page[limit]": 1
            },
            timeout=15
        )

        data = r.json().get("data", [])

        if not data:
            return None

        anime = data[0]["attributes"]

        poster = anime.get("posterImage", {})
        cover = anime.get("coverImage", {})

        return {
            "title": anime.get("canonicalTitle"),
            "image": poster.get("original"),
            "banner": cover.get("original"),
            "episodes": anime.get("episodeCount"),
            "score": anime.get("averageRating"),
            "year": anime.get("startDate", "")[:4],
            "genres": [],
            "synopsis": anime.get("synopsis")
        }

    except Exception as e:
        print("KITSU ERROR:", e)
        return None
