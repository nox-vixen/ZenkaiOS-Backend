import requests

ANILIST_URL = "https://graphql.anilist.co"


def graphql(query, variables=None):
    response = requests.post(
        ANILIST_URL,
        json={
            "query": query,
            "variables": variables or {}
        },
        timeout=30
    )

    response.raise_for_status()

    return response.json()["data"]


def get_anime(sort, limit=10):

    query = """
    query ($perPage:Int,$sort:[MediaSort]){

      Page(page:1, perPage:$perPage){

        media(
          type:ANIME
          sort:$sort
        ){

          id

          title{
            romaji
            english
          }

          description(asHtml:false)

          averageScore

          coverImage{
            extraLarge
          }

          bannerImage

          genres

          startDate{
            year
          }

        }

      }

    }
    """

    data = graphql(
        query,
        {
            "perPage": limit,
            "sort": sort
        }
    )

    anime = []

    for media in data["Page"]["media"]:

        anime.append({

            "id": media["id"],

            "title": media["title"]["english"] or media["title"]["romaji"],

            "description": (
    media.get("description", "")
    .replace("<br>", "<br><br>")
),

            "coverImage": media["coverImage"]["extraLarge"],

            "bannerImage": media.get("bannerImage"),

            "rating": media.get("averageScore"),

            "genres": media.get("genres", []),

            "year": media["startDate"]["year"]

        })

    return anime


def get_trending_anime(limit=5):
    return get_anime(["TRENDING_DESC"], limit)


def get_anime_details(anime_id):

    query = """
    query($id:Int){

      Media(id:$id,type:ANIME){

        id

        title{
          romaji
          english
        }

        description(asHtml:false)

        averageScore

        bannerImage

        genres

        episodes

        duration

        season

        seasonYear

        status

        format

        source

        coverImage{
          extraLarge
        }

        studios(isMain:true){
          nodes{
            name
          }
        }

        trailer{
          id
          site
        }

      }

    }
    """

    data = graphql(
        query,
        {
            "id": anime_id
        }
    )

    media = data["Media"]

    return {

        "id": media["id"],

        "title": media["title"]["english"] or media["title"]["romaji"],

        "description": media.get("description") or "",

        "coverImage": media["coverImage"]["extraLarge"],

        "bannerImage": media.get("bannerImage"),

        "rating": media.get("averageScore"),

        "genres": media.get("genres", []),

        "episodes": media.get("episodes"),

        "duration": media.get("duration"),

        "season": media.get("season"),

        "year": media.get("seasonYear"),

        "status": media.get("status"),

        "format": media.get("format"),

        "source": media.get("source"),

        "studios": [
            studio["name"]
            for studio in media.get("studios", {}).get("nodes", [])
        ],

        "trailer": media.get("trailer")

    }
