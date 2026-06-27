from backend.anilist import get_trending_anime


class HomeService:

    def get_home(self):

        featured = get_trending_anime(limit=5)

        return {
            "featured": {
                "lastUpdated": None,
                "items": featured
            },
            "sections": []
        }


home_service = HomeService()
