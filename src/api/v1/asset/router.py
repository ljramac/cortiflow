from pathlib import Path
from flask import Blueprint, request
from .controller import find, upload

assets_blueprint = Blueprint('assets', __name__, url_prefix='/api/v1/assets')


@assets_blueprint.route("/", methods=["GET", "POST"])
def index():
    try:
        if request.method == "POST":
            return upload(request)
        elif request.method == "GET":
            return find(request)
        else:
            return "Not implemented", 501
    except Exception as e:
        print(e)

        return "Internal Server Error", 500


if __name__ == '__main__':
    pass
