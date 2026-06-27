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

def get_trending_anime(limit=5):

    query = """
    query ($perPage:Int){

      Page(page:1, perPage:$perPage){

        media(

          type:ANIME

          sort:TRENDING_DESC

        ){

          id

          description(asHtml:false)

          genres

          averageScore

          bannerImage

          coverImage{

            extraLarge

          }

          title{

            romaji

            english

          }

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
            "perPage": limit
        }
    )

    anime = []

    for media in data["Page"]["media"]:

        anime.append({

            "id": media["id"],

            "title": media["title"]["english"] or media["title"]["romaji"],

            "description": media["description"] or "",

            "bannerImage": media["bannerImage"],

            "coverImage": media["coverImage"]["extraLarge"],

            "rating": media["averageScore"],

            "year": media["startDate"]["year"],

            "genres": media["genres"]

        })

    return anime
