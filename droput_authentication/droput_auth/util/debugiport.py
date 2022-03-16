from flask import current_app

DEBUG_MSG_CODES = {
    "100": "OK",
    "101": "Unsupported Media Type",
    "102": "DB connection error",
    "103": "User Not Found.",
    "104": "Request Validation Failed",
    "105": "Empty Data Supplied",
    "106": "User is already exist"
}


def debugiport(state={}, metadata={}, status=200, code=100, headers={}):
    data = state
    data.update(metadata)
    if current_app.debug:
        data["message"] = DEBUG_MSG_CODES[str(code)]
    data["code"] = code
    return data, status, headers

