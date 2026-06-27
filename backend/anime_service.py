from backend.anilist import get_anime_details


class AnimeService:

    def get(self, anime_id):

        anime = get_anime_details(anime_id)

        return {

            "id": anime["id"],

            "title": anime["title"],

            "description": anime["description"],

            "bannerImage": anime["bannerImage"],

            "coverImage": anime["coverImage"],

            "rating": anime["rating"],

            "year": anime["year"],

            "episodes": anime["episodes"],

            "duration": anime["duration"],

            "format": anime["format"],

            "status": anime["status"],

            "season": anime["season"],

            "genres": anime["genres"],

            "studios": anime["studios"],

            "trailer": anime["trailer"]

        }


anime_service = AnimeService()
