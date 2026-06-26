import requests

BASE_URL = "https://api.jikan.moe/v4"


def search(title):
    """
    Search an anime on Jikan.
    Returns the first result.
    """

    try:

        url = (
            f"{BASE_URL}/anime"
            f"?q={title}"
            "&limit=1"
        )

        r = requests.get(
            url,
            timeout=15
        )

        data = r.json()

        if not data.get("data"):
            return None

        anime = data["data"][0]

        return {
            "title": anime.get("title"),
            "image": anime["images"]["jpg"]["large_image_url"],
            "banner": anime.get("trailer", {}).get("images", {}).get("maximum_image_url"),
            "synopsis": anime.get("synopsis"),
            "score": anime.get("score"),
            "episodes": anime.get("episodes"),
            "year": anime.get("year"),
            "genres": [
                g["name"]
                for g in anime.get("genres", [])
            ]
        }

    except Exception as e:

        print("JIKAN ERROR:", e)

        return None


def top(limit=10):
    """
    Return top anime.
    """

    try:

        url = (
            f"{BASE_URL}/top/anime"
            f"?limit={limit}"
        )

        r = requests.get(
            url,
            timeout=15
        )

        data = r.json()

        result = []

        for anime in data["data"]:

            result.append({
                "title": anime["title"],
                "image": anime["images"]["jpg"]["large_image_url"]
            })

        return result

    except Exception as e:

        print(e)

        return []
