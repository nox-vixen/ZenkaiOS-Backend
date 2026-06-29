from moviebox_api.v1 import Search, SubjectType

from backend.session import get_session


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

        result = self.search(query)

        if not result.items:
            return None

        item = result.items[0]

        return {
            "subjectId": item.subjectId,
            "detailPath": item.detailPath,
            "subjectType": item.subjectType,
            "title": item.title,
            "cover": str(item.cover.url)
        }

moviebox_service = MovieBoxService()
