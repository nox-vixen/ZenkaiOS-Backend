from moviebox_api.v1 import Session

_session = None


def get_session():
    global _session

    if _session is None:
        _session = Session()

    return _session
