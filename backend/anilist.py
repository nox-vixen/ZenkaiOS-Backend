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
            "description": media["description"] or "",
            "coverImage": media["coverImage"]["extraLarge"],
            "bannerImage": media["bannerImage"],
            "rating": media["averageScore"],
            "genres": media["genres"],
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

        "description": media["description"] or "",

        "coverImage": media["coverImage"]["extraLarge"],

        "bannerImage": media["bannerImage"],

        "rating": media["averageScore"],

        "genres": media["genres"],

        "episodes": media["episodes"],

        "duration": media["duration"],

        "season": media["season"],

        "year": media["seasonYear"],

        "status": media["status"],

        "format": media["format"],

        "source": media["source"]

    }
