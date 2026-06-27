from backend.anilist import get_trending_anime, get_anime

class HomeService:

    def get_home(self):

        featured = get_trending_anime(limit=5)

        return {
            "featured": {
                "lastUpdated": None,
                "items": featured
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


home_service = HomeService()
