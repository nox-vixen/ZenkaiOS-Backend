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
        "id": "trending",
        "title": "Trending Now",
        "viewAll": "/anime/trending",
        "items": get_anime(["TRENDING_DESC"], 10)
    },
    {
        "id": "popular",
        "title": "Most Popular",
        "viewAll": "/anime/popular",
        "items": get_anime(["POPULARITY_DESC"], 10)
    },
    {
        "id": "top_rated",
        "title": "Top Rated",
        "viewAll": "/anime/top",
        "items": get_anime(["SCORE_DESC"], 10)
    },
    {
        "id": "new",
        "title": "Newest Releases",
        "viewAll": "/anime/new",
        "items": get_anime(["START_DATE_DESC"], 10)
    },
    {
        "id": "favorites",
        "title": "Fan Favorites",
        "viewAll": "/anime/favorites",
        "items": get_anime(["FAVOURITES_DESC"], 10)
    }
]

        }


home_engine = HomeEngine()
