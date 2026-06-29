from flask import Blueprint, jsonify

stream_bp = Blueprint("stream", __name__)

@stream_bp.route("/debug/moviebox")
def debug_moviebox():

    import inspect
    import moviebox_api.v1 as v1

    return jsonify({
        "classes": [
            name
            for name, obj in inspect.getmembers(v1)
            if inspect.isclass(obj)
        ]
    })
