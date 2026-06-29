from moviebox_api.v1 import Search, SubjectType

from backend.session import get_session

from backend.cache_service import cache_service

class MovieBoxService:

    async def search_async(self, query):

        session = get_session()

        search = Search(
            session=session,
            query=query,
            subject_type=SubjectType.ALL,
            page=1,
            per_page=10
        )

        return await search.get_content_model()

    def search(self, query):

        import asyncio

        return asyncio.run(
            self.search_async(query)
        )


    def first_match(self, query):

        key = query.lower().strip().replace(" ", "_")

        cached = cache_service.load(key)

        if cached:

            print(f"[CACHE] {query}")

            return cached

        print(f"[API] {query}")

        result = self.search(query)

        if not result.items:
            return None

        item = result.items[0]

        data = {

            "subjectId": item.subjectId,

            "detailPath": item.detailPath,

            "subjectType": item.subjectType,

            "title": item.title,

            "cover": str(item.cover.url)

        }

        cache_service.save(key, data)

        print("[CACHE SAVED]", key)

        return data

moviebox_service = MovieBoxService()
