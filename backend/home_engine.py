from backend.cache_reader import read_cache


class HomeEngine:

    def build(self):

        cache = read_cache()

        print("CACHE DATA:")
        print(cache)

        if cache is None:

            return {
                "featured": {
                    "items": []
                },
                "sections": []
            }

        featured_items = []

        for anime in cache["featured"]:

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
                    "items": cache["trending"]
                },

                {
                    "id": "popular",
                    "title": "Most Popular",
                    "viewAll": "/anime/popular",
                    "items": cache["popular"]
                },

                {
                    "id": "top_rated",
                    "title": "Top Rated",
                    "viewAll": "/anime/top",
                    "items": cache["top_rated"]
                },

                {
                    "id": "new",
                    "title": "Newest Releases",
                    "viewAll": "/anime/new",
                    "items": cache["new"]
                },

                {
                    "id": "favorites",
                    "title": "Fan Favorites",
                    "viewAll": "/anime/favorites",
                    "items": cache["favorites"]
                }

            ]

        }


home_engine = HomeEngine()
