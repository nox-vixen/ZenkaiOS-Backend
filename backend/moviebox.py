from moviebox_client import moviebox_get
import asyncio
import json


def get_home():

    raw = asyncio.run(
        moviebox_get(
            "/wefeed-h5api-bff/home?host=moviebox.ph"
        )
    )

    return json.loads(raw["text"])
