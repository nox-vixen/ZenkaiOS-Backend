import asyncio

from moviebox_api.v1 import Search
from moviebox_api.v1 import SubjectType

from backend.session import get_session


class SearchService:

    async def search_async(self, keyword):

        search = Search(
            session=get_session(),
            query=keyword,
            subject_type=SubjectType.MOVIES
        )

        results = await search.get_content_model()

        output = []

        for item in results.items:

            output.append({

                "id": item.subjectId,

                "title": item.title,

                "image": str(item.cover.url),

                "description": item.description,

                "year": str(item.releaseDate),

                "duration": item.duration,

                "genres": item.genre

            })

        return output

    def search(self, keyword):
        return asyncio.run(
            self.search_async(keyword)
        )


search_service = SearchService()
