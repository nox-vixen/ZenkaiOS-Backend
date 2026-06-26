import requests


def get_banner():

    r = requests.get(
        "https://api.jikan.moe/v4/top/anime",
        timeout=20
    )

    data = r.json()

    banners = []

    for anime in data["data"][:5]:

        banners.append({

            "title": anime["title"],

            "image": anime["images"]["jpg"]["large_image_url"],

            "synopsis": anime.get(
                "synopsis",
                ""
            )[:150]

        })

    return banners
