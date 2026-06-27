from backend.anime_service import anime_service


class AnimeEngine:

    def build(self, anime_id):

        return anime_service.get(anime_id)


anime_engine = AnimeEngine()
