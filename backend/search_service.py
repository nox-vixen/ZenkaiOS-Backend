from moviebox_api.v1 import Search, SubjectType

from backend.session import get_session


class SearchService:

    async def search_async(
        self,
        keyword,
        subject_type=SubjectType.MOVIES,
        page=1,
        per_page=24
    ):

        session = get_session()

        search = Search(
            session=session,
            query=keyword,
            subject_type=subject_type,
            page=page,
            per_page=per_page
        )

        return await search.get_content_model()

    def search(
        self,
        keyword,
        subject_type=SubjectType.MOVIES,
        page=1,
        per_page=24
    ):

        import asyncio

        return asyncio.run(
            self.search_async(
                keyword,
                subject_type,
                page,
                per_page
            )
        )


search_service = SearchService()
