from backend.search_service import search_service
from backend.anilist import get_trending_anime


class HomeService:

    def __init__(self):
        pass

    def featured(self):

        featured = []

        trending = get_trending_anime(limit=5)

        for anime in trending:

            results = search_service.search(
                anime["title"]
            )

            if not results.items:
                continue

            moviebox = results.first_item

            featured.append({

                "id": moviebox.subjectId,

                "title": moviebox.title,

                "description": anime["description"],

                "image": anime["bannerImage"],

                "poster": anime["coverImage"],

                "rating": anime["rating"],

                "year": anime["year"],

                "genres": anime["genres"]

            })

        return featured


home_service = HomeService()
