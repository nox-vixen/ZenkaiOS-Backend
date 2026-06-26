import asyncio

from moviebox_api.v1 import (
    Search,
    Session,
    SubjectType,
)


def search(title):
    try:

        async def run():

            session = Session()

            search = Search(
                session=session,
                query=title,
                subject_type=SubjectType.TV_SERIES,
            )

            results = await search.get_content_model()

            if not results.items:
                return None

            return results.items[0]

        return asyncio.run(run())

    except Exception as e:

        print("MOVIEBOX ERROR:", e)

        return None
