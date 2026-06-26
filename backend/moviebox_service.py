import asyncio

from moviebox_api.v1 import (
    Search,
    Session,
    SubjectType
)


class MovieBoxService:

    async def search_async(self, keyword):

        session = Session()

        search = Search(
            session=session,
            query=keyword,
            subject_type=SubjectType.MOVIES
        )

        results = await search.get_content_model()

        return results

    def search(self, keyword):

        return asyncio.run(
            self.search_async(keyword)
        )


moviebox = MovieBoxService()
