import requests

URL = "https://graphql.anilist.co"

def search(title):
    query = """
    query ($search: String) {
      Media(search: $search, type: ANIME) {
        title {
          romaji
          english
        }
        coverImage {
          extraLarge
        }
        bannerImage
        episodes
        averageScore
        description(asHtml:false)
        genres
        seasonYear
      }
    }
    """

    variables = {
        "search": title
    }

    try:
        r = requests.post(
            URL,
            json={
                "query": query,
                "variables": variables
            },
            timeout=15
        )

        data = r.json()["data"]["Media"]

        return {
            "title": data["title"]["english"] or data["title"]["romaji"],
            "image": data["coverImage"]["extraLarge"],
            "banner": data["bannerImage"],
            "episodes": data["episodes"],
            "score": data["averageScore"],
            "year": data["seasonYear"],
            "genres": data["genres"],
            "synopsis": data["description"]
        }

    except Exception as e:
        print("ANILIST ERROR:", e)
        return None
