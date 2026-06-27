from backend.anilist import get_trending_anime, get_anime

class HomeEngine:

    def build(self):

        featured = get_trending_anime(5)

        featured_items = []

        for anime in featured:

            featured_items.append({

                "id": anime["id"],

                "title": anime["title"],

                "description": anime["description"],

                "bannerImage": anime["bannerImage"],

                "coverImage": anime["coverImage"],

                "rating": anime["rating"],

                "year": anime["year"],

                "genres": anime["genres"],

                "watchNow": f"/watch/{anime['id']}",

                "myList": False

            })

        return {

            "featured": {

                "items": featured_items

            },

            "sections": [
    {
        "id": "trending_now",
        "title": "Trending Now",
        "viewAll": "/anime/trending",
        "items": get_anime(["TRENDING_DESC"], 10)
    }
]

        }


home_engine = HomeEngine()
