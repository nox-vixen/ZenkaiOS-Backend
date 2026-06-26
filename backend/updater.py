from backend.cache import (
    get,
    save
)

from backend.jikan import (
    search as jikan_search
)

from backend.moviebox import (
    search as moviebox_search
)


def update_one_anime(title):

    cached = get(title)

    if cached:

        print("[CACHE]", title)

        return cached

    print("[NEW]", title)

    moviebox = moviebox_search(title)

    jikan = jikan_search(title)

    anime = {
        "title": title,
        "moviebox": moviebox,
        "jikan": jikan
    }

    save(title, anime)

    return anime
