from backend.anilist import get_trending_anime


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

            "sections": []

        }


home_engine = HomeEngine()
