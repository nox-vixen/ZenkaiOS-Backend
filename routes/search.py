from flask import Blueprint, jsonify, request

import asyncio

from moviebox_api.v1 import Search
from moviebox_api.v1 import Session
from moviebox_api.v1 import SubjectType

search_bp = Blueprint("search", __name__)


@search_bp.route("/api/search")
def search():

    keyword = request.args.get("q", "").strip()

    if not keyword:
        return jsonify([])

    async def run():

        session = Session()

        search = Search(
            session=session,
            query=keyword,
            subject_type=SubjectType.MOVIES
        )

        results = await search.get_content_model()

        output = []

        for item in results.items:

            output.append({
                "id": item.subjectId,
                "title": item.title,
                "image": str(item.cover.url),
                "description": item.description,
                "year": str(item.releaseDate),
                "duration": item.duration,
                "genres": item.genre
            })

        return output

    return jsonify(asyncio.run(run()))
