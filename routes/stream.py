from flask import Blueprint, jsonify
from pathlib import Path
import asyncio
import inspect

from backend.moviebox_service import moviebox_service
from backend.session import get_session

import moviebox_api.v1 as mb
from moviebox_api.v1 import (
    Search,
    SubjectType,
    TVSeriesDetails,
    DownloadableTVSeriesFilesDetail,
)

stream_bp = Blueprint("stream", __name__)


# ============================================================
# Main API
# ============================================================

@stream_bp.route("/api/moviebox/search/<path:title>")
def moviebox_search(title):

    result = moviebox_service.first_match(title)

    if result is None:
        return jsonify({
            "success": False,
            "message": "Anime not found"
        }), 404

    return jsonify({
        "success": True,
        "data": result
    })


# ============================================================
# Debug
# ============================================================

@stream_bp.route("/debug/cache")
def debug_cache():

    folder = Path("cache/moviebox")

    return jsonify({
        "files": [
            file.name
            for file in folder.glob("*.json")
        ]
    })


@stream_bp.route("/debug/classes")
def debug_classes():

    return jsonify({
        "classes": dir(mb)
    })


@stream_bp.route("/debug/tv_signature")
def debug_tv_signature():

    return jsonify({
        "signature": str(
            inspect.signature(TVSeriesDetails)
        )
    })


@stream_bp.route("/debug/download_signature")
def debug_download_signature():

    return jsonify({
        "signature": str(
            inspect.signature(
                DownloadableTVSeriesFilesDetail
            )
        )
    })


@stream_bp.route("/debug/download_methods")
def debug_download_methods():

    return jsonify({
        "methods": [
            name
            for name, value in inspect.getmembers(
                DownloadableTVSeriesFilesDetail
            )
            if callable(value)
            and not name.startswith("_")
        ]
    })


# ============================================================
# TV Details
# ============================================================

@stream_bp.route("/debug/download/<path:title>/<int:season>/<int:episode>")
def debug_download(title, season, episode):

    session = get_session()

    search = Search(
        session=session,
        query=title,
        subject_type=SubjectType.ALL,
        page=1,
        per_page=1
    )

    result = asyncio.run(search.get_content_model())

    if not result.items:
        return jsonify({"error": "Not found"}), 404

    item = result.items[0]

    download = DownloadableTVSeriesFilesDetail(
        session=session,
        item=item
    )

    data = asyncio.run(
        download.get_content_model(
            season=season,
            episode=episode
        )
    )

    return data.model_dump_json()

# ============================================================
# Download / Episode Resources
# ============================================================

@stream_bp.route("/debug/download/<path:title>/<int:season>/<int:episode>")
def debug_download(title, season, episode):

    session = get_session()

    search = Search(
        session=session,
        query=title,
        subject_type=SubjectType.ALL,
        page=1,
        per_page=1
    )

    result = asyncio.run(
        search.get_content_model()
    )

    if not result.items:
        return jsonify({
            "error": "Anime not found"
        }), 404

    item = result.items[0]

    download = DownloadableTVSeriesFilesDetail(
        session=session,
        item=item
    )

    data = asyncio.run(
        download.get_content_model(
            season=season,
            episode=episode
        )
    )

    return jsonify(data.model_dump())


@stream_bp.route("/debug/download_signature2")
def debug_download_signature2():

    return jsonify({
        "signature": str(
            inspect.signature(
                DownloadableTVSeriesFilesDetail.get_content_model
            )
        )
    })
