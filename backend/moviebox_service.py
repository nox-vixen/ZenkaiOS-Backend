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


moviebox_service = MovieBoxService()
