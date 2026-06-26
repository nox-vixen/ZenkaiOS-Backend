from moviebox_client import moviebox_get
import asyncio
import json


def get_home():

    raw = asyncio.run(
        moviebox_get(
            "/wefeed-h5api-bff/home?host=moviebox.ph"
        )
    )

    parsed = json.loads(raw["text"])

    anime = []

    for section in parsed["data"]["operatingList"]:

        title = section.get("title", "").lower()

        if "anime" not in title:
            continue

        for subject in section.get("subjects", []):

            anime.append({

                "title": subject.get("title"),

                "image": subject.get("cover", {}).get("url"),

                "rating": subject.get("imdbRatingValue"),

                "year": subject.get("releaseDate"),

            })

    return anime
