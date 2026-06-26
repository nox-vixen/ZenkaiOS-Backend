import asyncio
import json

from moviebox_client import moviebox_get


class MovieBox:

    async def _request(self, endpoint):

        raw = await moviebox_get(endpoint)

        return json.loads(raw["text"])

    def home(self):

        return asyncio.run(

            self._request(
                "/wefeed-h5api-bff/home?host=moviebox.ph"
            )

        )
     
    def search(self, keyword):

    return asyncio.run(

        self._request(
            f"/search?keyword={keyword}"
        )

    )

moviebox = MovieBox()
