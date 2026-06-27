from moviebox_api.v1 import MovieDetails

from backend.session import get_session


class DetailsService:

    async def details_async(self, target):

        session = get_session()

        details = MovieDetails(
            target,
            session=session
        )

        return await details.get_content_model()

    def details(self, target):

        import asyncio

        return asyncio.run(
            self.details_async(target)
        )


details_service = DetailsService()
