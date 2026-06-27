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
        "id": "trending_now",
        "title": "Trending Now",
        "viewAll": "/anime/trending",
        "items": get_anime(["TRENDING_DESC"], 10)
    }
]
        }


home_service = HomeService()
