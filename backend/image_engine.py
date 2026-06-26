from backend import jikan
from backend import anilist
from backend import kitsu

PROVIDERS = [
    jikan.search,
    anilist.search,
    kitsu.search
]


def search(title):
    """
    Search every provider until one succeeds.
    """

    for provider in PROVIDERS:

        try:

            result = provider(title)

            if result and result.get("image"):

                print(
                    "[IMAGE]",
                    provider.__module__,
                    title
                )

                return result

        except Exception as e:

            print(provider.__module__, e)

    return None
