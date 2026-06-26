from flask import Blueprint
from backend.moviebox_service import moviebox

search_bp = Blueprint(
    "search",
    __name__
)


@search_bp.route("/api/search-test")
def search_test():

    result = moviebox.search("One Piece")

    return {
        "type": str(type(result)),
        "repr": str(result)[:500]
    }
