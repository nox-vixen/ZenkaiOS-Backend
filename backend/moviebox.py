import asyncio

from moviebox_client import moviebox_get


class MovieBox:

    def test(self, endpoint):
        return asyncio.run(moviebox_get(endpoint))


moviebox = MovieBox()
