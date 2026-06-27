from moviebox_api.v1 import DownloadableMovieFilesDetail

from backend.session import get_session


class StreamService:

    async def streams_async(self, movie_details):

        session = get_session()

        downloadable = DownloadableMovieFilesDetail(
            session=session,
            movie_details=movie_details
        )

        return await downloadable.get_content_model()

    def streams(self, movie_details):

        import asyncio

        return asyncio.run(
            self.streams_async(movie_details)
        )


stream_service = StreamService()
