from flask import Blueprint, jsonify

stream_bp = Blueprint("stream", __name__)

@stream_bp.route("/debug/moviebox")
def debug_moviebox():

    from moviebox_api.v1 import Search
    import inspect

    return jsonify({

        "signature": str(

            inspect.signature(Search)

        )

    })
